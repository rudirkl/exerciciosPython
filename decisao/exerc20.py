#!/usr/bin/python3

RES = ["APROVADO", "REPROVADO", "APROVADO COM DISTINCAO"]
CON = ["A","B","C","D","E"]
SAIDA = '''
media = {media}
conceito = {conceito}
resultado = {resultado}
'''

def conceito(x: float, y: float, z: float):
    media = (x+y+z)/3
    if (media == 10):
        return(SAIDA.format(conceito=CON[0], media=media, resultado=RES[2] ))
    elif (media >= 9 and media <= 10):
        return(SAIDA.format(conceito=CON[0], media=media, resultado=RES[0] ))
    
    elif (media >= 7 and media < 9):
        return(SAIDA.format(conceito=CON[1], media=media, resultado=RES[0]))
    
    elif (media >= 6.0 and media < 7):
        return(SAIDA.format(conceito=CON[2], media=media, resultado=RES[1]))
        
    elif (media >= 4.0 and media < 6.0):
        return(SAIDA.format(conceito=CON[3], media=media, resultado=RES[1]))

    elif (media < 4  and media >= 0):
        return(SAIDA.format(conceito=CON[4], media=media, resultado=RES[1]))
    
    else:
        return("Invalido")

def main():
    try:
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))
        print(conceito(nota1, nota2, nota3))
    except:
        print("Deu errado")

if __name__ == "__main__":
    main()
