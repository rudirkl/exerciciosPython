#!/usr/bin/python3

SAIDA ='''
Notas de cem = {cem}
Notas de cinquenta = {cinquenta}
Notas de dez = {dez}
Notas de cinco = {cinco}
Notas de um = {um}
'''

def calculo(x: int):
    cem = int(x/100)
    x = x%100

    cinq = int(x/50)
    x = x%50

    dez = int(x/10)
    x = x%10

    cinc = int(x/5)
    x = x%5

    um = x

    return(SAIDA.format(cem=cem, cinquenta=cinq, dez=dez, cinco=cinc, um=um))

def main():
    try:
        valor = int(input("Digite o valor do saque: "))
        if (valor >= 10 and valor < 600):
            print(calculo(valor))
        else:
            print("valor invalido")
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
