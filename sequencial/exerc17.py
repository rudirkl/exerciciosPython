#!/usr/bin/python3

import math

PRECOL = 80.0
PRECOG = 25
CAPACIDADEL = 18
CAPACIDADEG = 3.6
MARGSEG = 1.1

def calcularLatas(x: float):
    litros = x/6 * MARGSEG
    latas = litros / CAPACIDADEL
    latas = math.ceil(latas) # arredondar para cima
    total = latas * PRECOL
    return("Numero de latas: "+str(latas), "Valor R$"+str(total))

def calcularGal(x: float):
    litros = x/6 * MARGSEG
    galoes = litros / CAPACIDADEG
    galoes = math.ceil(galoes) # arredondar para cima
    total = galoes * PRECOG
    return("Numero de galoes: "+str(galoes), "Valor R$"+str(total))

def calcularMisto(x: float):
    litros = x/6 * 1.1
    mistLata = int(litros/18.0)
    mistGal = int((litros - (mistLata * 18)) / 3.6)
    if litros - (mistLata * 18) % 3.6 !=0:
        mistGal += 1
    total = (mistLata * 80) + (mistGal * 25)
    return("Numero de latas: "+str(mistLata),"Numero de galoes: "+str(mistGal),"Valor total: R$"+str(total))

def main():
    tamanho = float(input("Digite o tamanho em metros quadrados"))
    print(calcularLatas(tamanho))
    print(calcularGal(tamanho))
    print(calcularMisto(tamanho))

if __name__ == "__main__":
    main()

