#!/usr/bin/python3

def maior(x: float, y: float, z: float):
    if (x > y and x > z):
        if (y < z):
            res = "primeiro maior e segundo menor"
        else:
            res = "primeiro maior e terceiro menor"
    elif ( y > x and y > z):
        if (x > z):
            res = "o segundo e maior e terceiro menor"
        else:
            res = "segundo maior e primeiro menor"
    elif (z > x and z > y):
        if (x > y):
            res = "o terceiro e maior e segundo menor"
        else:
            res = " terceiro e maior e primeiro menor"
    else:
            res = "sao iguais"
    return (res)


def main():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    num3 = float(input("Digite o terceiro numero: "))
    print(maior(num1, num2, num3))

if __name__ == "__main__":
    main()
