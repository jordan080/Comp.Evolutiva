import sys
import random
import numpy as np

''' lambda: tamanho da populacao
mu: numero de pais selecionados
lambda / mu: numero de filhos gerados para cada pai selecionado
(lambda, mi)
[(5, 19), (2, 10), (5, 20) ...]
[(5, 20), (5, 19), (2, 10) ...]
[19237, 10203, 1823918, ...] '''

def printInd(populacao):
  for i in range(0, len(populacao[0])):
    print('\n')
    for j in range(0, 20):
      print(str(round(populacao[i][j])), end = ",")
          
# Selecao
def selecao(populacao):
  selecionados = random.choices(populacao, weights=tuple(range(20, 0, -1)), k=2)
  return selecionados

# Fitness
def Fitness(populacao, equation):
  fitness = []
  for i in range(0, len(populacao)):
    aux = 0
    for j in range(0, 20):
      aux = ((populacao[i][j] ** equation[j][1]) * equation[j][0]) + aux
    fitness.append(aux)
  return (sorted(fitness))

#Cruzamento
def Cruzamento(pai, mae):
  auxPai = []
  auxMae = []

  splitPai = np.array_split(pai, 5)
  splitMae = np.array_split(mae, 5)

  for i in range(0, len(splitPai), 2):
    auxPai.append(list(splitPai[i]))
  for i in range(1, len(splitMae), 2):
    auxMae.append(list(splitMae[i]))
  auxPai = [r for l in auxPai for r in l] # [1, 2, 3, 4, 5, 6]
  auxMae = [r for l in auxMae for r in l] # [4, 45, 5, 6, 7, 0]
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
  for i in range(0, len(filho)):
    filho[i] = filho[i] + random.gauss(0, 0.0005)

  return filho

# populacao inicial

def gerarPopulacaoInicial(tamanhoPopulacao):
  minValue = 0
  maxValue = 10
  populacao = []
  
  for i in range(0, tamanhoPopulacao):
    individuo = []
    for j in range(0, 20):
      num = random.uniform(minValue, maxValue)
      individuo.append(num)
    populacao.append(individuo)
  return populacao

if __name__ == '__main__':
  tamanhoPopulacao = 20
  geracoes = 5000

  equation = [(3,20), (8,19), (7,18), (3,17), (12,16), (9,15), (10,14), (8,13), (12,12), (1,11), (3,10), (8,9), (4,8), (9,7), (7,6), (9,5), (9,4), (9,3), (11,2), (12,1)]

  populacao = gerarPopulacaoInicial(tamanhoPopulacao)
  fitness = Fitness(populacao, equation)
  
  while (geracoes > 0):
    populacaoFilhos = []
    for i in range(0, len(populacao)):
      pai, mae = selecao(populacao)
      filhoCruzamento = Cruzamento(pai, mae)
      Mutacao(filhoCruzamento)
      populacaoFilhos.append(filhoCruzamento)
    populacao = populacaoFilhos
    fitness = Fitness(populacao, equation)
    geracoes -= 1

  print(populacao[0], end = "\n")
  print(round(fitness[0]), end = "\n")
  
    
    