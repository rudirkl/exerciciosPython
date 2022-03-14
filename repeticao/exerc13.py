#!/usr/bin/python3

def calculo(x: int, y: int):
    pot = 1
    for i in range(y):
        pot *= x
        i += 1
    print(x,"^",y,"=",pot)

def main():
    base = int(input("Digite a base: "))
    exp = int(input("Digite o expoente: "))
    calculo(base,exp)

if __name__ == "__main__":
    main()
