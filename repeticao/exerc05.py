#!/usr/bin/python3

def calculo(a: int, aT: float, b: int, bT: float, cont: int, anos: int):
    a = a + (a*aT)
    b = b + (b*bT)
    if (a > b):
        anos = anos + 1
        cont =1
    else:
        anos = anos+1
    return(a,aT,b,bT,cont,anos)

def main():
    try:
        cont = 0
        anos = 0
        a = int(input("Digite a populacao de A: "))
        aT = float(input("Digite a taxa de crescimento de A: "))
        b = int(input("Digite a populacao de B: "))
        bT = float(input("Digite a taxa de crescimento de B: "))
        while (cont == 0):
            a, aT, b, bT, cont, anos = calculo(a, aT, b, bT, cont, anos)
        print("Demora: "+str(anos)+" anos")
    except:
     print("Algo deu errado.")

if __name__ == "__main__":
    main()
