#!/usr/bin/python3

import sys

def calculo(x):
    return (72.7*x) - 58 

def main():
    if len(sys.argv) > 1:
        altura = float(sys.argv[1])
    else:
        altura = float(input("Digite sua altura"))

    print (calculo(altura))

if __name__ == "__main__":
    main()
