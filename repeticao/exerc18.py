#!/usr/bin/python3

import random

SAIDA = '''
Maior = {maior}
Menor = {menor}
Soma = {soma}
'''

def calculo():
    maior = -9999
    menor = 9999
    soma = 0
    mem = []
    mem = random.sample(range(10), k=5)
    res = len(mem)
    print(mem)
    for i in range(0,res):
        if(mem[i] > maior):
            maior = mem[i]
        elif(mem[i] < menor):
            menor = mem[i]
        soma += mem[i]
    return(SAIDA.format(maior=maior,menor=menor,soma=soma))

def main():
    print(calculo())

if __name__ == "__main__":
    main()
