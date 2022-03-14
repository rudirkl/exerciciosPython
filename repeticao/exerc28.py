#!/usr/bin/python3

TURMAS = []
SAIDA = '''
Total gasto em CDs = R${soma}
Total de CDs = {turmas}
Media de valores por CD = R${media}
'''

def calculo(x: int):
    global TURMAS
    cont = 0
    soma = 0
    while (cont < x):
        num = float(input(f"Digite o valor do CD {cont}: "))
        TURMAS.append(num)
        cont += 1
    for i in range(x):
        soma += TURMAS[i]
    media = soma/x
    print(SAIDA.format(soma=soma,turmas=x,media=media))

def main():
    turma = int(input("Digite o numero de CDs: "))
    calculo(turma)

if __name__ == "__main__":
    main()
