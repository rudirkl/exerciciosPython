#!/usr/bin/python3

COD = []
ALT = []
PES = []

SAIDA = '''
Maior altura = Codigo {codMaiorAltura} altura {maiorAltura}
Menor altura = Codigo {codMenorAltura} altura {menorAltura}
'''

def calculo():
    maiorPeso = -9999
    menorPeso = 9999
    maiorAltura = -9999
    menorAltura = 9999
    codMaiorAltura = 0
    codMenorAltura = 0
    codMaiorPeso = 0
    codMenorPeso = 0
    somaPeso = 0
    somaAltura = 0
    lenCod = len(COD)
    for i in range(lenCod):
        somaPeso += PES[i]
        somaAltura += ALT[i]
        if(maiorAltura < ALT[i]):
            codMaiorAltura = COD[i]
            maiorAltura = ALT[i]
        if(menorAltura > ALT[i]):
            codMenorAltura = COD[i]
            menorAltura = ALT[i]
        if(maiorPeso < PES[i]):
            codMaiorPeso = COD[i]
            maiorPeso = PES[i]
        if(menorPeso > PES[i]):
            codMenorPeso = COD[i]
            menorPeso = PES[i]
    mediaPeso = somaPeso/lenCod
    mediaAltura = somaAltura/lenCod
    print(codMenorAltura, codMaiorAltura, codMaiorPeso, codMenorPeso, maiorPeso, menorPeso, maiorAltura, menorAltura)



    print(somaPeso)

def main():
    while True:
        cod = int(input("Digite o fcodigo: "))
        if (cod == 0):
            break
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))
        COD.append(cod)
        ALT.append(altura)
        PES.append(peso)
    calculo()
if __name__ == "__main__":
    main()
