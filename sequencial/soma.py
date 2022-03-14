#!/usr/bin/python3

def soma(x: float, y: float) -> float:
    return x + y

def main():
    num1 = float(input("Digite o primeiro numero= "))
    num2 = float(input("Digite o segundo numero= "))
    r = soma(num1, num2)
    print(r)

if __name__=="__main__":
    main()
