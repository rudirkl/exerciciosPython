#!/usr/bin/python3

DIAN = ["seg","ter","que","qui","sex","sab","dom"]

def verDia(x: int ):
    if (x > -1 and x <=6):
        return(DIAN[x])
    else:
        return("invalido")

def main():
    try:
        dia = int(input("Digite um dia da semana: "))
        dia = dia - 1
        print(verDia(dia))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
