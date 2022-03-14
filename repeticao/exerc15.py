#!/usr/bin/python3

def calculo(x = int):
    cont = 2
    i = 0
    ult = 1
    pen = 0
    while (cont <= x):
        i = ult + pen
        pen = ult
        ult = i
        cont += 1
    print(i)

def main():
    num = int(input("Qual termo do fibonacci? "))
    calculo(num)

if __name__ == "__main__":
    main()
