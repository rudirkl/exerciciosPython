#!/usr/bin/python3

def calculo(x: int, y: int):
    z = 0
    if (y < x):
        z = y
        y = x
        x = z
    x = x+1
    for x in range(x,y):
        print(x)

def main():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    calculo(num1,num2)

if __name__ == "__main__":
    main()
