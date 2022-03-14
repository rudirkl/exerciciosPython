#!/usr/bin/python3

def salario(x: float, y: float) -> float:
    return x * y

def main():
    valHora = float(input("Digite o valor da hora= "))
    horas = float(input("Digite quantidades de hora= "))
    print('O salario mensall e: {} '.format(salario(valHora, horas)))

if __name__=="__main__":
    main()
