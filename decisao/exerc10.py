#!/usr/bin/python3


def hora(x: str):
    if (x == 'm'):
        res = "Bom dia"
    elif (x == 'v'):
        res = "boa tarde"
    elif (x == 'n'):
        res = "boa noite"
    else:
        res = "opcao invalida"
    return(res)


def main():
    turno = str(input("Digite o turno que voce estuda: "))
    turno = turno.lower()
    print(hora(turno))

if __name__ == "__main__":
    main()

