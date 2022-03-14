#!/usr/bin/python3

def calcula(x: int):
    if (x%4 == 0 and x%100 != 0 ):
        return("E bissexto")
    elif (x%4 == 0 and x%100 == 0 and x%400 == 0):
        return("E bissexto")
    else:
        return("Nao e bisexto")


def main():
    try:
        ano = int(input("Digite um ano: "))
        print(calcula(ano))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
