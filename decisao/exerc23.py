#!/usr/bin/python3

def calculo(x: float):
    if (x%1 == 0):
        return("Inteiro")
    else:
        return("decimal")

def main():
    try:
        num = float(input("digite um numero: "))
        print(calculo(num))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
