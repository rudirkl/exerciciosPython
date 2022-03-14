#!/usr/bin/python3

SAIDA = '''
Numeros pares = {pares}
Numeros impares = {impares}
Total de par = {tPar}
Total impares = {tImpar}
'''

def calculo():
    i = 0
    impares = []
    pares = []
    while(i!=10):
        i += 1
        num = int(input("Digite um numero: "))
        if(num%2 == 0):
            pares.append(num)
        else:
            impares.append(num)
    parT = len(pares)
    impT = len(impares)
    return(SAIDA.format(pares=pares,impares=impares,tPar=parT,tImpar=impT))

def main():
    print(calculo())

if __name__ == "__main__":
    main()
