#!/usr/bin/python3

NUM = []

def calculo():
    print("As notas sao:", NUM)
    tam = len(NUM)
    soma =0
    for i in range(tam):
        soma += int(NUM[i])
    print("A media das notas e:",soma/tam)

def main():
    i = 0
    esc = True
    try:
        while(esc):
            numero = str(input("Digite um numero para nota, n para calcular as notas ou q para sair "))
            if (numero == "q"):
                esc = False
                break
            elif (numero == "n"):
                esc = False
                calculo()
            elif not numero.isdigit():
                print("Somente numeros ou q para sair")
            else:
                NUM.append(numero)
                i +=1
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
