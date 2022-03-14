#!/usr/bin/python3

def conversao(x: float) -> float:
    return x * 100

def main():
    num1 = float(input("Digite o primeiro numero= "))
    print(conversao(num1))

if __name__=="__main__":
    main()

