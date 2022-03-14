#!/usr/bin/python3

SAIDA = '''
sem desconto = {sem}
com desconto = {com}
'''

def calculo(x: int, y: str):
    res1 = 0
    res2 = 0
    if (x <= 20 and y == "a"):
        res1 = (1.90*x)
        res2 = res1
        res2 -= res1*0.03
        return(SAIDA.format(sem=res1, com=res2))
    elif (x > 20 and y == "a"):
        res1 = (1.90*x)
        res2 = res1
        res2 -= res1*0.05
        return(SAIDA.format(sem=res1, com=res2))
    elif (x <= 20 and y == "g"):
        res1 = (2.5*x)
        res2 = res1
        res2 -= res1*0.04
        return(SAIDA.format(sem=res1, com=res2))
    elif (x > 20 and y == "g"):
        res1 = (2.5*x)
        res2 = res1
        res2 -= res1*0.06
        return(SAIDA.format(sem=res1, com=res2))
    else:
        return("algum valor invalido")

def main():
    try:
        qtd = int(input("Quantos litros: "))
        tipo = str(input('''
        Escolha o tipo de combustivel A para alcool e G para gasolina: 
        '''))
        tipo = tipo.lower()
        print (calculo(qtd, tipo))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
