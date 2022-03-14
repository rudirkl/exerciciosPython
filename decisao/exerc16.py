#!/usr/bin/python3

import math

def calculo(a: int, b: int, c: int):
    delta = b*b - (4*a*c)

    if (delta < 0):
        print("Nao pode ter raizes reais")
    elif (delta == 0):
        raiz = -b / (2*a)
        return('Delta=0 , raiz=', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return('Raizes: ', raiz1, ' e ',raiz2)

def main():
    
    try:
        a = int(input("Informe o valor de a: "))

        if (a==0):
            print("A igual a zero nao e equacao do segundo grau")
        else:
            b = int(input("Digite o valor de b: "))
            c = int(input("Digite o valor de c: "))
            print(calculo(a,b,c))
    except:
        print("Algo dei errado")

if __name__ == "__main__":
    main()
