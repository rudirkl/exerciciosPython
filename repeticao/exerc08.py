#!/usr/bin/python3

SAIDA = '''
Numeros = {numeros}
Maior = {maior}
Soma = {soma}
Media = {media:0.2f}
'''

def calculo():
    maior = 0
    cont = 0
    soma = 0
    numeros = []
    while(cont != 5):
        num = int(input("Digite um numero: "))
        if(num > maior):
            maior = num
        numeros.append(num)
        soma = soma+num
        cont = cont+1
    media = soma/5
    return(SAIDA.format(maior=maior,soma=soma,media=media,numeros=numeros))

def main():
    print(calculo())
    
if __name__ == "__main__":
    main()
