#!/usr/bin/bash

def calculo(x: int):
    i = x
    for i in range(x,-1,-1):
        res = x*i
        print(x,"*",i,"=",res)

def main():
    num = int(input("Digite um numero: "))
    calculo(num)

if __name__ == "__main__":
    main()

