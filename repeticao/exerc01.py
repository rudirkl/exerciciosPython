#!/usr/bin/python3

def calculo(x: int, y: float):
    if (y >= 0 and y <= 10):
        x = 1
    else:
        print("valor invalido")
    return(x,y)

def main():
    try:
        cont = 0
        while(cont == 0):
            val = float(input("Digite o valor da nota: "))
            cont, val = calculo(cont,val)
        print("Valor da nota: "+str(val))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
