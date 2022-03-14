#!/usr/bin/python3

import sys

def salario(x: float, y: float):
    bruto = x * y
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - (ir + inss + sindicato)
    return (bruto, ir, inss, sindicato, liquido)

def main():
    if len(sys.argv) > 2:
        valorHora = float(sys.argv[1])
        numHoras = float(sys.argv[2])
        salario(valorHora, numHoras)
        print (salario(valorHora, numHoras))
    else:
        valorHora = float(input("Digite o valor da hora"))
        numHoras = float(input("Digite o numero de horas"))
        print (salario(valorHora, numHoras))

if __name__ == "__main__":
    main()
