#!/usr/bin/python3

def maior(x: float, y: float, z: float):
    if (x > y and x > z):
        res = "primeiro maior"
    elif ( y > x and y > z):
        res = "o segundo e maior"
    elif (z > x and z > y):
        res = "o terceiro e maior"
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
