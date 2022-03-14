#!/usr/bin/python3

PRM = []

def calculo(x: int):
    global PRM
    for i in range(x+1):
        if (i%2==1 and i!=2):
            PRM.append(i)
    print(PRM)

def main(): 
    num = int(input("Digite um numero: "))
    calculo(num)

if __name__ == "__main__":
    main()
