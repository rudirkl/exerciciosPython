#!/usr/bin/python3

SAIDA = '''
Compara duas strings
String 1: {x}
String 2: {y}
Tamanho da string 1: {valx}
Tamanho da string 2: {valy}
As duas string sao de tamanhos {tamanho}
As duas strings possuem conteudo {conteudo}
'''

def compara(x: str, y: str):
    valx = len(x)
    valy = len(y)
    if(x == y):
        tam = "iguais"
        con = "iguais"
    elif(x != y) and (valx == valy):
        tam = "iguais"
        con = "diferentes"
    else:
        tam = "diferentes"
        con = "diferentes"
    print(SAIDA.format(x=x,y=y,valx=valx,valy=valy,tamanho=tam,conteudo=con))

def main():
    str1 = str(input("Digite a primeira string: "))
    str2 = str(input("Digite a segunda string: "))
    compara(str1,str2)

if __name__ == "__main__":
    main()
