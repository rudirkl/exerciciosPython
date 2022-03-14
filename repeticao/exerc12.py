#!/usr/bin/python3

def calculo(x: int):
    for i in range(1,11):
        res = x*i
        print(x," X ",i," = ",res)

def main():
    num = int(input("Digite o numero que quiser saber a taboada: "))
    calculo(num)

if __name__ == "__main__":
    main()
