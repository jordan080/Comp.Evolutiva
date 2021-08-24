import random

operadores = ['&', '|']
res_experado = [1, 1, 0, 1, 0, 0, 0, 0]

def Fitness(expression):
    aux = []
    Fit = 0
    for p in range(0,2):
        for q in range(0,2):
            for r in range(0,2):
                x = eval(expression)
                aux.append(x)

    for i in range(len(res_experado)):
        if aux[i] == res_experado[i]:
            Fit += 1
    return Fit

def GerarExp(n):
    exp = ""
    for i in range(n):
        wr = random.randint(1,2) 
        we = random.randint(1,6)

        if wr == 1:
            if we == 1:
                exp += 'p & '
            elif we == 2:
                exp += 'q & '
            elif we == 3:
                exp += 'r & '
            elif we == 4:
                exp += '~ p & '
            elif we == 5:
                exp += '~ q & '
            else:
                exp += '~ r & '

        else:
            if we == 1:
                exp += 'p | '
            elif we == 2:
                exp += 'q | '
            elif we == 3:
                exp += 'r | '
            elif we == 4:
                exp += '~ p | '
            elif we == 5:
                exp += '~ q | '
            else:
                exp += '~ r | '

    exp = exp[:-2]
    return exp


if __name__ == "__main__":
    populacao = []
    valores = []

    for i in range(10):
        n = random.randint(3, 9)
        populacao.append(GerarExp(n))
    
    for j in range(len(populacao)):
        valores.append(Fitness(populacao[j]))
    
    print(valores)


