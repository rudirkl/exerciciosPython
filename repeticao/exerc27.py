#!/usr/bin/python3

TURMAS = []
SAIDA = '''
Total de alunos = {soma}
Total de turmas = {turmas}
Media de alunos por turmas = {media}
'''

def calculo(x: int):
    global TURMAS
    cont = 0
    soma = 0
    while (cont < x):
        num = int(input(f"Digite o numero de alunos na turma {cont}: "))
        if (num > 40):
            print("valor invalido")
        else:
            TURMAS.append(num)
            cont += 1
    for i in range(x):
        soma += TURMAS[i]
    media = soma/x
    print(SAIDA.format(soma=soma,turmas=x,media=media))

def main():
    turma = int(input("Digite o numero de turmas: "))
    calculo(turma)

if __name__ == "__main__":
    main()
