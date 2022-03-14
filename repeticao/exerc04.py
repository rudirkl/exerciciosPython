#!/usr/bin/python3

A = 80000
B = 200000

def calculo(x: int, y: int):
    global A 
    global B 
    A = A + (A*0.03)
    B = B + (B*0.015)
    if (A > B):
        y = y+1
        x =1
    else:
        y = y+1
    return(x,y)

def main():
    try:
        cont = 0
        anos = 0
        while (cont == 0):
            cont, anos = calculo(cont, anos)
        print("Demora: "+str(anos)+" anos")
    except:
        print("Algo deu errado.")

if __name__ == "__main__":
    main()
