#!/usr/bin/python3

def calculo(x: int):
    if (x%2 != 0):
        result = "Impar"
    else:
        result = "Par"
    return(result)

def main():
    try:
        valor = int(input("Digite um valor inteiro: "))
        print(calculo(valor))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
