import gym
import sys
import random
import numpy as np

env = gym.make('CartPole-v0')

def ambiente():
	observation = env.reset()
	network.get_positions(observation)
	count = 0
	while True:
			action = network.predict()
			observation, reward, done, _ = env.step(action)
			count += reward
			if count == 200:
				return True, count
			elif done:
				return False, count

class MLP:
	input_layer_size = 4
	first_hidden_layer_size = 4
	second_hidden_layer_size = 3
	output_layer_size = 1

	def __init__(self):
		pass
		
	def get_weights(self, pesos):
		self.weights = [None, None, None]

		self.weights[0] = np.array([pesos, pesos, pesos, pesos])
		self.weights[1] = np.array([pesos, pesos, pesos])
		self.weights[2] = np.array([pesos])

		print(self.weights)
		
	def get_positions(self, posicoes):
		self.posicoes = posicoes

	def ff_apply_inputs(self, posicoes):
		self.node_values = [None, None, None, None]
		self.node_values[0] = np.array([0.0, 0.0, 0.0, 0.0])
		self.node_values[1] = np.array([0.0, 0.0, 0.0, 0.0])
		self.node_values[2] = np.array([0.0, 0.0, 0.0])
		self.node_values[3] = np.array([0.0])

		self.node_values[0][0] = posicoes[0]
		self.node_values[0][1] = posicoes[1]
		self.node_values[0][2] = posicoes[2]
		self.node_values[0][3] = posicoes[3]

		self.node_values[0] = np.array([posicoes[0], posicoes[1], posicoes[2], posicoes[3]])

	def ff_compute_first_hidden_layer(self):
			for i in range(0, self.first_hidden_layer_size):
					column_vector = self.weights[0][:, [i]]

					new_node_value = np.matmul(column_vector, np.array(self.node_values[0]))[0]
					new_node_value = self.activation_function(new_node_value)
					self.node_values[1][i] = new_node_value

	def ff_compute_second_hidden_layer(self):
			for i in range(0, self.second_hidden_layer_size):
					column_vector = self.weights[1][:, [i]]

					new_node_value = np.matmul(column_vector, np.array(self.node_values[1]))[0]
					new_node_value = self.activation_function(new_node_value)
					self.node_values[2][i] = new_node_value

	def ff_compute_output_layer(self):
			for i in range(0, self.output_layer_size):
					column_vector = self.weights[2][:, [i]]

					new_node_value = np.matmul(column_vector, np.array(self.node_values[2]))[0]
					self.node_values[3][i] = new_node_value

	def activation_function(self, x):
			return np.maximum(0,x)
		
	def predict(self):
		self.ff_apply_inputs(self.posicoes)
		self.ff_compute_first_hidden_layer()
		self.ff_compute_second_hidden_layer()
		self.ff_compute_output_layer()

		output_value = self.node_values[3][0]
		if output_value > 0.5:
			return 1
		else:
			return 0

def printInd(populacao):
	for i in range(0, len(populacao[0])):
		print('\n')
		for j in range(0, 20):
			print(str(round(populacao[i][j])), end = ",")
					
# Selecao
def selecao(populacao):
	#print(populacao)
	#Selecionar 50% pelo método da roleta
	#selecionados = random.choices(populacao, weights=tuple(range(20, 0, -1)), k=2)
	selecionados = random.sample(list(populacao), k=2)
	return selecionados

# Fitness: UTILIZAR A REDE NEURAL
def Fitness(populacao):
	Fitness = []
	flag = None

	for i in range(len(populacao)):
			peso = populacao[i]
			network.get_weights(peso)
			flag, fitness = ambiente()
			Fitness.append(fitness)
		
	sorted(Fitness, reverse = True)
	return flag, Fitness

#Cruzamento
def Cruzamento(pai, mae):
	auxPai = []
	auxMae = []
	
	#seleciona a metade à esquerda do pai
	midPai = len(pai) // 2
	for i in range(0, midPai):
		auxPai.append(pai[i])
		
	#seleciona a metade à direita da mae
	midMae = len(mae) // 2
	for j in range(midMae, len(mae)):
		auxMae.append(mae[j])
	
	#gera o filho
	filho = auxPai + auxMae
	return filho

#Mutacao Populacao
def mutarPopulacao(populacao, taxaMutacao):
	for i in range(0, len(populacao)):
		if (random.random() < taxaMutacao):
			populacao[i] = Mutacao(populacao[i])
	return populacao

#Mutacao
def Mutacao(filho):
	print(filho)
	for i in range(0, len(filho)):
		filho[i] = random.random()
	return filho

# populacao inicial

def gerarPopulacaoInicial(tamanhoPopulacao):
	# gerar a populacao inicial
	populacao = []
	
	for i in range(tamanhoPopulacao):
		individuo = []
		for j in range(4):
			n = random.random()
			individuo.append(n)
		populacao.append(individuo)
	return populacao


if __name__ == '__main__':
	tamanhoPopulacao = 50
	geracoes = 300
	network = MLP()
	
	populacao = np.asarray(gerarPopulacaoInicial(tamanhoPopulacao))
	fitness = Fitness(populacao)
	flag = False
	
	while (flag == False and geracoes > 0):
		populacaoFilhos = np.empty(50)
		for i in range(0, len(populacao)):
			pai, mae = selecao(populacao)
			#print("#a")
			#print(pai, mae)
			filhoCruzamento = Cruzamento(pai, mae)
			np.append(populacaoFilhos, filhoCruzamento)
		populacaoFilhos = mutarPopulacao(populacaoFilhos, 0.01)
		populacao = populacaoFilhos
		#print("#b")
		#print(populacao)
		flag, fitness = Fitness(populacao)
		geracoes -= 1

print('Pendulo equilibrado com sucessos')
print(fitness[0])
print(populacao[0])