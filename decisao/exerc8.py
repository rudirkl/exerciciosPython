#!/usr/bin/python3

def maior(x: float, y: float, z: float):
    if (x < y and x < z):
        res = "primeiro mais barato"
    elif ( y < x and y < z):
        res = "o segundo mais barato"
    elif (z < x and z < y):
        res = "o terceiro e mais barato"
    elif (x <= y and x < z):
        res = "primeiro e segundo iguais"
    elif (x <= z and x < y):
        res = "primeiro e terceiro iguais"
    elif (y <= z and y < x):
        res = "segundo e terceiro iguais"
    else:
        res = "tdos sao iguais"
    return (res)


def main():
    num1 = float(input("Digite o primeiro preco: "))
    num2 = float(input("Digite o segundo preco: "))
    num3 = float(input("Digite o terceiro preco: "))
    print(maior(num1, num2, num3))

if __name__ == "__main__":
    main()
