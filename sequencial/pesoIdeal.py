#!/usr/bin/python3

import sys

def calculo(x: float, y: str):
    if (y == "h"):
        return (72.7*x) - 58
    if (y == "m"):
        return (62.1*x) - 44.7

def main():
    
    if len(sys.argv) > 2:
        sexo = str(sys.argv[1])
        altura = float(sys.argv[2])
    else:
        sexo = str(input("Digite h para home ou m para mulher"))
        altura = float(input("Digite sua altura"))

    print (calculo(altura,sexo))

if __name__ == "__main__":
    main()

