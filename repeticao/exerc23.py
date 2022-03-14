#!/usr/bin/python3

def calculo(x: int):
    if (x%2==0):
        print(f"{x} nao e primo e foi executada uma divisao")
    elif (x==1) or(x==2):
        print(f"{x} e primo e nao foi executada nenhuma divisao para encontrar.")
    else:
        primo = True
        cont = 1
        for i in range(3,x,2):
            if (x%i==0):
                primo = False
                break
        if primo:
            print(f"{x} e primo e foram executadas {cont} divisoes")
        else:
            print(f"{x} nao e primo e foram executadas {cont} divisoes")

def main():
    num = int(input("Digite um numero: "))
    calculo(num)

if __name__ == "__main__":
    main()
