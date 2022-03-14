#!/usr/bin/python3

def calculo(x: float, y: float, z: int):
    if(z==0):
        w = x+y
    elif(z==1):
        w = x-y
    elif(z==2):
        w = x/y
    elif(z==3):
        w = x*y
    else:
        print("numero invalido")
        return 1
    if (w%1 == 0):
        tipo = "Inteiro"
    else:
        tipo = "decimal"
    if (w <0):
        sinal = "negativo"
    else:
        sinal = "positivo"
    if (w%2 == 0):
        resto = "par"
    else:
        resto = "impar"
    return(w, tipo, sinal, resto)

def main():
    try:
        num1 = float(input("digite um numero: "))
        num2 = float(input("digite outro numero: "))
        op = int(input('''
        Digite uma operacao
        0 = soma
        1 = subtracao
        2 = divisao
        3 = miltiplicacao
        '''))
        print(calculo(num1, num2, op))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
