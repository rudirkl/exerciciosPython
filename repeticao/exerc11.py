#!/usr/bin/python3

def calculo(x: int, y: int):
    z = 0
    soma = 0
    if (y < x):
        z = y
        y = x
        x = z
    for i in range((x+1),y):
        soma = soma + i
        print(i)
    print("A soma e:",soma)

def main():
    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        calculo(num1,num2)
    except:
        print("Algo deu errado.")

if __name__ == "__main__":
    main()
