#!/usr/bin/python3

def calcpeso (x: float):
    if (x > 50):
        res = (x -50) * 4
        return ("multa de R$"+str(res))
    else:
        return "tudo ok"

def main():
    peso = float(input("Digite o peso"))
    print (calcpeso(peso))

if __name__ == "__main__":
    main()
