import random, copy

class Perceptron:

	def __init__(self, entradas, desejado, taxa_aprendizado=0.1, epocas=1000):

		self.entradas = entradas # matriz com as colunas de cada um dos átomos
		self.desejado = desejado # valores desejados da ultima coluna, na qual contém a expressão
		self.taxa_aprendizado = taxa_aprendizado # taxa de aprendizado (entre 0 e 1)
		self.epocas = epocas # número de épocas
		self.num_entradas = len(entradas) # quantidade de entradas
		self.num_elementos = len(entradas[0]) # quantidade de elementos por entrada
		self.pesos = [] # vetor de pesos

	def treinar(self):

		# inicia o vetor de pesos com valores aleatórios
		for i in range(self.num_elementos):
			self.pesos.append(random.random())

		# inicia o contador de epocas
		num_epocas = 0

		while True:

			erro = False # o erro inicialmente inexiste

			# para todas as entradas de treinamento
			for i in range(self.num_entradas):
				soma = 0
				for j in range(self.num_elementos):
					soma += self.pesos[j] * self.entradas[i][j]

				# obtém a saída da rede utilizando a função de ativação
				saida = self.sinal(soma)

				# verifica se a saída da rede é diferente da saída desejada
				if saida != self.desejado[i]:

					# calcula o erro: subtração entre a saída desejada e a saída da rede
					erro_aux = self.desejado[i] - saida

					# faz o ajuste dos pesos para cada elemento da elemento
					for j in range(self.num_elementos):
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.entradas[i][j]

					erro = True # ainda existe erro

			# incrementa o número de épocas
			num_epocas += 1

			# critério de parada é pelo número de épocas ou se não existir erro
			if num_epocas > self.epocas or not erro:
				break

	def testar(self, testes):

		resultado = []

		for i in range(self.num_entradas):
			soma = 0
			for j in range(self.num_elementos):
				soma += self.pesos[j] * testes[i][j]

			y = self.sinal(soma)
			resultado.append(y)
		
		return resultado


	# função de ativação: degrau bipolar (sinal)
	def sinal(self, u):
		return 0 if u <= 0 else 1
	
	def gerar_tabela(self, testes, resultado):
		res = []

		for i in range(self.num_entradas):
			aux = testes[i]
			aux.append(resultado[i])
			res.append(aux)

		print("| {} | {} | {} | {} | ".format('p', 'q', 'r', '(q ^ p) v (p ^ ~r)'))

		for i in range(self.num_entradas):
			print("| {} | {} | {} |         {}          | ".format(res[i][0], res[i][1], res[i][2], res[i][4]))
		
#matriz com as colunas de cada um dos átomos
entradas = [[0, 0, 0, 1],
			[0, 0, 1, 1],
			[0, 1, 0, 1],
			[0, 1, 1, 1],
			[1, 0, 0, 1],
			[1, 0, 1, 1],
			[1, 1, 0, 1],
			[1, 1, 1, 1]]

# valores desejados da ultima coluna, na qual contém a expressão
desejado = [0, 0, 0, 0, 1, 0, 1, 1]

# conjunto de entradas de testes
testes = copy.deepcopy(entradas)

# cria uma rede Perceptron
rede = Perceptron(entradas = entradas, desejado = desejado, taxa_aprendizado = 0.1, epocas = 1000)

# treina a rede
rede.treinar()

# testa a rede e gera a ultima coluna da tabela
resultado = rede.testar(testes)

# gera a tabela verdade
rede.gerar_tabela(testes, resultado)