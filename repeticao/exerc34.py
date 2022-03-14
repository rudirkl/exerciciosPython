#!/usr/bin/python3

def calculo(x: int):
    for i in range(2,x):
        if(x%i==0):
            print("Nao e primo")
            break
    else: 
        print("e primo")

def main():
    num = int(input("Digite um nunmero: "))
    calculo(num)

if __name__ == "__main__":
    main()
