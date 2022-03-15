#!/usr/bin/python3

MES = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
SAIDA = '''
Data de nascimento: {dia1}/{mes1}/{ano1}
Voce nasceu em: {dia1} de {mes2} de {ano1}
'''

def calculo(x: int, y: int, z: int):
    return(SAIDA.format(dia1=x, mes1=y, ano1=z, mes2=MES[y-1]))

def main():
    dia = int(input("Digite o dia de nascimento: ")) 
    mes = int(input("Digite o mes de nascimento: "))
    ano = int(input("Digite o ano de nascimento: "))
    print(calculo(dia, mes, ano))

if __name__ == "__main__":
    main()
