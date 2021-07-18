import random
import operator

def printPopulacao(populacao):
  # printa no terminal a populacao gerada
  for i in range(0, len(populacao)):
    for j in range(0, len(populacao[i]) - 1):
      print(f'({populacao[i][j].fromC}, {populacao[i][j].toC}) -> ', end = '')
    print(f'({populacao[i][len(populacao[i]) - 1].fromC}, {populacao[i][len(populacao[i]) - 1].toC})\n')


class Passo:
  # classe que define um passo de cada aresta do grafo
  def __init__ (self, fromCity, toCity):
    self.fromC = fromCity
    self.toC = toCity


def gerarPopulacaoInicial(populacao, tamanhoPopulacao, lista):
  # gerar a populacao inicial
  i = tamanhoPopulacao
  while(i > 0):
    n = random.randint(2, 11)
    populacao.append(random.sample(lista, n))
    i = i - 1
  return populacao



# Classe de fitness
class Fitness:
  def __init__(self, rota):
    self.rota = rota
    self.fitness = 0.00
    self.distancia = 0
  
  # método para calcular a distancia da rota
  def distanciaRota(self):
    self.distancia = len(self.rota)
  
  # método para retornar o grau de ajuste do individuo
  def fitnessRota(self):
    if self.fitness == 0:
      self.fitness = (1 / float(self.distanciaRota()))
    return self.fitness
  

# ranqueamento dos individuos da populacao
def ranqueamentoRotas(populacao):
  fitness = {}
  for i in range(0, len(populacao)):
    fitness[i] = Fitness(populacao[i]).distanciaRota()
  return sorted(fitness.items(), key = operator.itemgetter(1), reverse = True)


def cruzamento(pai, mae):
  auxPai = []
  auxMae = []
  
  #seleciona a metade à direita do pai
  midPai = len(pai) // 2
  for i in pai[midPai:]:
    auxPai[i] = pai[i]
    
  #seleciona a metade à direita da mae
  midMae = len(mae) // 2
  for j in mae[midMae:]:
    auxPai[j] = mae[j]
  
  #gera o filho
  filho = auxPai + auxMae
  return filho


# verificar cidades inicial, final e do doente
def avaliar(individuo, cidadeInicial, cidadeAlvo):
  flag = False
  
  # verificando se começa e termina na mesma cidade
  if individuo[0].fromC != cidadeInicial or individuo[len(individuo) - 1].toC != cidadeInicial:
    return False
  
  # verificando se a cidadeAlvo está na rota
  for i in individuo:
    if i.fromC == cidadeAlvo or i.toC == cidadeAlvo:
      flag = True
  
  # verificando se o caminho é válido
  for i in individuo:
    if i.toC != i.fromC:
      flag = False
  
  return flag
  
  
a = Passo(1, 2)
b = Passo(2, 6)
c = Passo(6, 7)
d = Passo(7, 1)
e = Passo(6, 2)
f = Passo(6, 4)
g = Passo(7, 4)
h = Passo(4, 5)
i = Passo(4, 3)
j = Passo(3, 4)
k = Passo(5, 7)

cidadeInicial = 1
cidadeAlvo = 6

listaPassos = [a, b, c, d, e, f, g, h, i, j, k]
interacoes = 25

'''individuoQualquer = [a, b, c, d]
1 -> 2 -> 6 -> 7 -> 1'''

populacaoInicial = []
inicial = gerarPopulacaoInicial(populacaoInicial, 10, listaPassos)
# printPopulacao(inicial)

for i in populacaoInicial:
  if avaliar(populacaoInicial[i], cidadeInicial, cidadeAlvo) == False:
    populacaoInicial.remove(populacaoInicial[i])

while(intercoes > 0):
  ranqueamentoRotas(populacaoInicial)
  cruzamento(populacaoInicial[0], populacaoInicial[1])
  #...
  interacoes = interacoes - i
