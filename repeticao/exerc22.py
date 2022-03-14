#!/usr/bin/python3

def calculo(x: int):
    cont = 0
    for i in range(2,x):
        if(x%i==0):
            print("Divisivel por:",i)
            print("Nao e primo")
            cont +=1
    else:
        if(cont==0):
            print("e primo")

def main():
    num = int(input("Digite um nunmero: "))
    calculo(num)

if __name__ == "__main__":
    main()
