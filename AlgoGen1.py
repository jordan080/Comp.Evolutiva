import random
import operator

# printa no terminal a populacao gerada
def printPopulacao(populacao):
  for i in range(0, len(populacao)):
    for j in range(0, len(populacao[i]) - 1):
      print(f'({populacao[i][j].fromC}, {populacao[i][j].toC}) -> ', end = '')
    print(f'({populacao[i][len(populacao[i]) - 1].fromC}, {populacao[i][len(populacao[i]) - 1].toC})\n')


def printRota(rota):
  for i in range(len(rota) - 1):
    print(f'{rota[i].fromC} -> ', end='')
  print(f'{rota[len(rota) - 1].fromC} -> {rota[len(rota) - 1].toC}')


class Passo:
  # classe que define um passo de cada aresta do grafo
  def __init__ (self, fromCity, toCity):
    self.fromC = fromCity
    self.toC = toCity

def printIndividuo(individuo):
  for i in range(0, len(individuo)):
    print(f'({individuo[i].fromC}, {individuo[i].toC})  ', end='')
  print('\n')

def gerarPopulacaoInicial(tamanhoPopulacao, lista):
  # gerar a populacao inicial
  populacao = []
  flag = True
  while flag:
    n = random.randint(2, 11)
    individuo = random.sample(lista, n)
    
    if avaliar(individuo, cidadeInicial, cidadeAlvo):
      populacao.append(individuo)
      if len(populacao) == tamanhoPopulacao:
        flag = False
    
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
    return self.distancia
  
  # método para retornar o grau de ajuste do individuo
  def fitnessRota(self):
    if self.fitness == 0:
      self.fitness = (1 / float(self.distanciaRota()))
    return self.fitness
  

# ranqueamento dos individuos da populacao
def ranqueamentoRotas(populacao):
  fitness = {}
  for i in range(0, len(populacao)):
    fitness[i] = Fitness(populacao[i]).fitnessRota()
  return sorted(fitness.items(), key = operator.itemgetter(1), reverse = True)


def cruzamento(pai, mae):
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


def mutarPopulacao(populacao, taxaMutacao, cidadeInicial, cidadeAlvo):
  populacaoMutada = []
  for i in range(0, len(populacao)):
    if (random.random() < taxaMutacao):
      individuoAuxiliar = populacao[i]
      individuoMutado = mutar(individuoAuxiliar)
      if avaliar(individuoMutado, cidadeInicial, cidadeAlvo):
        populacaoMutada.append(individuoMutado)
      else:
        populacaoMutada.append(populacao[i])
    else:
      populacaoMutada.append(populacao[i])
  return populacaoMutada


def mutar(seq):
  idx = range(len(seq))
  i1, i2 = random.sample(idx, 2)
  seq[i1], seq[i2] = seq[i2], seq[i1]
  return seq
		

# verificar cidades inicial, final e do doente
def avaliar(individuo, cidadeInicial, cidadeAlvo):
  flag = False
  
  # verificando se começa e termina na mesma cidade
  if (individuo[0].fromC != cidadeInicial) or (individuo[len(individuo) - 1].toC != cidadeInicial):
    return False
  
  # verificando se a cidadeAlvo está na rota
  for i in individuo:
    # print(i.fromC)
    if i.fromC == cidadeAlvo or i.toC == cidadeAlvo:
      flag = True

  for i in range(0, (len(individuo) - 1)):
    if individuo[i].toC != individuo[i+1].fromC:
      flag = False

  return flag
  

# SELEÇÃO
def selecao(populacaoRanqueada):
  selecionados = random.choices(populacaoRanqueada, weights=(10, 9, 8, 7, 6), k=2)
  return selecionados

def comparaRotas(rota1, rota2):
  if len(rota1) != len(rota2):
    return False
  for i in range(len(rota1)):
    if rota1[i].fromC != rota2[i].fromC or rota1[i].toC != rota2[i].toC:
      return False
  return True

# main
if __name__ == '__main__':
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

  geracoes = 70
  listaPassos = [a, b, c, d, e, f, g, h, i, j, k]

  cidadeAlvo = int(input('Em que cidade o doente está? '))
  cidadeInicial = 1

  populacaoInicial = gerarPopulacaoInicial(5, listaPassos)

  flag = 1
  melhorRota = populacaoInicial[ranqueamentoRotas(populacaoInicial)[0][0]]
  
      
  #loop de intereacoes
  while(geracoes > 0):
    print(f'Geração {71 - geracoes}: ', end='')
    printRota(melhorRota)
    rotasRanqueadas = ranqueamentoRotas(populacaoInicial)
    
    if comparaRotas(populacaoInicial[0], melhorRota):
      flag += 1
      if flag == 10:
        print('EVOLUÇÃO INTERROMPIDA, A SOLUÇÃO JÁ FOI ENCONTRADA')
        break
    else:
      if (len(populacaoInicial[0]) < len(melhorRota)):
        melhorRota = populacaoInicial[0]
      flag = 1

    populacaoFilhos = []
  
    for i in range(0, len(populacaoInicial)):
      pai, mae = selecao(populacaoInicial)
      filhoResultadoCruzamento = cruzamento(pai, mae)
      populacaoFilhos.append(filhoResultadoCruzamento)
      
    populacaoInicial = mutarPopulacao(populacaoFilhos, 0.05, cidadeInicial, cidadeAlvo)

    geracoes -= 1
  print('Essa é a melhor rota: ')
  printRota(melhorRota)
