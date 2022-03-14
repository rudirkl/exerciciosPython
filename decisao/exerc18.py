#!/usr/bin/python3

def calculo(x: int, y: int, z: int):
    if ((x > 00 and x < 32 ) and (y > 00 and y <13)):
        return("data valida: "+str(x)+"/"+str(y)+"/"+str(z))
    else:
        return("invalida")

def main():
    try:
        data = input("Digite a data no formato dd/mm/aaaa somente numeros: ")
        dia = int(data[0:2])
        mes = int(data[2:4])
        ano = int(data[4:8])
        print(calculo(dia,mes,ano))
    except:
        print("algo deu errado")

if __name__ == "__main__":
    main()
