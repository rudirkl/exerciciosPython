#!/usr/bin/python3

C1= 0
C2 = 0
C3 = 0

SAIDA = '''
Candidato 1 = {C1}
Candidato 2 = {C2}
Candidato 3 = {C3}
'''

def votar(x: int):
    global C1,C2,C3
    if (x == 1):
        C1 += 1
    elif (x == 2):
        C2 += 1
    elif (x == 3):
        C3 += 1
    else:
        print("valor invalido")

def main():
    num = int(input("Digite o numero de eleitores: "))
    for i in range(num):
        voto = int(input("Digite o numero para votar: "))
        votar(voto)
    print(SAIDA.format(C1=C1,C2=C2,C3=C3))

if __name__ == "__main__":
    main()
