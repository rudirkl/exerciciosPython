#!/usr/bin/python3

NUM = []

def calculo():
    print("As idades sao:", NUM)
    tam = len(NUM)
    soma =0
    for i in range(tam):
        soma += int(NUM[i])
    media = soma/tam
    print("A media e:",media)
    if (media >= 0 and media <= 25):
        print("Turma jovem!")
    elif (media >= 26 and media <= 60):
        print("Turma adulta!")
    elif (media > 60):
        print("Turma idosa!")
    else:
        print("Resultado invalido.")

def main():
    i = 0
    esc = True
    try:
        while(esc):
            numero = str(input("Digite uma idade, n para calcular as idade ou q para sair "))
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
