#!/usr/bin/python3

import math

PRECOL = 80.0
CAPACIDADE = 18

def calcular(x: float):
    litros = x/3
    latas = litros / CAPACIDADE
    latas = math.ceil(latas) # arredondar para cima
    total = latas * PRECOL
    return(latas, "R$"+str(total))


def main():
    tamanho = float(input("Digite o tamanho em metros quadrados"))
    print(calcular(tamanho))

if __name__ == "__main__":
    main()
