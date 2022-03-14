#!/usr/bin/python3

MEM = []

SAIDA = '''
Maior = {maior:.2f}
Menor = {menor:.2f}
Media = {media:.2f}
'''

def calculo():
    global MEM
    maior = -9999
    menor = 9999
    soma = 0
    res = len(MEM)
    for i in range(0,res):
        if(MEM[i] > maior):
            maior = MEM[i]
        if(MEM[i] < menor):
            menor = MEM[i]
        soma += MEM[i]
    media = soma/res
    return(SAIDA.format(maior=maior,menor=menor,media=media))

def main():
    num = 0
    while(num != 9999):
        num = float(input("Digite uma temperatura ou 9999 para sair: "))
        if(num==9999):
            break
        else:
            MEM.append(num)
    print(calculo())

if __name__ == "__main__":
    main()
