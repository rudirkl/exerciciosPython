#!/usr/bin/python3

SAIDA = '''
Montar a taboada de: {x}
Comecar por: {y}
Terminar em: {z}

Vou montar a taboada de {x} comecando em {y} e terminando em {z}
'''

def calculo(x: int, y: int, z: int):
    print(SAIDA.format(x=x,y=y,z=z))
    for i in range(y,z+1):
        res = x*i
        print(x," X ",i," = ",res)

def main():
    num = int(input("Digite o numero que quiser saber a taboada: "))
    ini = int(input("Digite onde iniciar: "))
    fin = int(input("Digite onde terminar: "))
    calculo(num,ini,fin)

if __name__ == "__main__":
    main()
