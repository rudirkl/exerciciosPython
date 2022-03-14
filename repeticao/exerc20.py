#!/usr/bin/bash

def calculo(x: int):
    i = x
    for i in range(x,-1,-1):
        res = x*i
        print(x,"*",i,"=",res)

def main():
    num = 0 
    while(num != 99):
        num = int(input("Digite um numero entre 1 e 15 ou 99 para sair: "))
        if(num > 0 and num < 16):
            calculo(num)
        else:
            print("Valor invalido")

if __name__ == "__main__":
    main()

