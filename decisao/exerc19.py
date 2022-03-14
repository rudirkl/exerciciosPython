#!/usr/bin/python3

TERMO = ["centenas","centena","dezenas","dezena","unidades","unidade"]
SAIDA = '''
{centena}  {centenas}
{dezena}  {dezenas}
{unidade}  {unidades}
'''
def calculo(x: str, y: int):
    if (y == 3):
        cen = int(x[0:1])
        dez = int(x[1:2])
        uni = int(x[2:3])
        if (cen > 1):
            cenBol = 0
        else:
             cenBol = 1
        if (dez > 1):
            dezBol = 2
        else:
            dezBol = 3
        if (uni > 1):
            uniBol = 4
        else:
            uniBol = 5
        return(SAIDA.format(centena = cen, centenas = TERMO[cenBol], dezena = dez, dezenas = TERMO[dezBol], unidade = uni, unidades = TERMO[uniBol]))

    elif (y == 2):
        dez = int(x[0:1])
        uni = int(x[1:2])
        if (dez > 1):
            dezBol = 2
        else:
            dezBol = 3
        if (uni > 1):
            uniBol = 4
        else:
            uniBol = 5
        return(SAIDA.format(centena = "", centenas = "", dezena  = dez, dezenas = TERMO[dezBol], unidade = uni, unidades = TERMO[uniBol]))
    
    elif (y == 1):
        uni = int(x[0:1])
        if (uni > 1):
            uniBol = 4
        else:
            uniBol = 5
        return(SAIDA.format(centena = "", centenas = "", dezena  = "", dezenas = "", unidade = uni, unidades = TERMO[uniBol]))

    else:
        return("numero invalido")

def main():
    try:
        num = int(input("Digite um numero entre 0 e 1000: "))
        if (num >= 0 and num <1000):
            numStr = str(num)
            qtd = len(numStr)
            print(num, numStr)
            print(calculo(numStr,qtd))
        else:
            print("numero invalido")
    except:
        print("algo deu errado")

if __name__ == "__main__":
    main()
