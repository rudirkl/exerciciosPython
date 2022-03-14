#!/usr/bin/python3

def maior(x: float, y: float):
    if (x > y):
        res = "primeiro maior que segundo"
    elif ( x < y):
        res = "o segundo e maior que o primeiro"
    else:
        res = "os dois sao iguais"
    return (res)


def main():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(maior(num1, num2))

if __name__ == "__main__":
    main()
