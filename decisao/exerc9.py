#!/usr/bin/python3

LISTA = []
QTD = 3

def maior(x):
    x.sort(reverse = True)
    return(x)


def main():
    for i in range(QTD):
        elemento = int(input("Digite o numero {} ".format(i)))
        LISTA.append(elemento)
    print(maior(LISTA))

if __name__ == "__main__":
    main()
