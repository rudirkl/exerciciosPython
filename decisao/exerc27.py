#!/usr/bin/python3

SAIDA = '''
total de macas = {totalMac}KG R${ValorMac:0.2f}
total de morangos = {totalMor}Kg R${ValorMor:0.2f}
valor total = R${total:0.2f}
Valor total com desconto = R${totalDesc:0.2f}
'''

def calculo(x: float, y: float):
    if (x <= 5 and x > 0):
        totalMac = x*1.80
    elif (x > 5):
        totalMac = x*1.50
    else:
        totalMac = 0
    if (y <= 5 and y > 0):
        totalMor = y*2.50
    elif (y > 5):
        totalMor = y*2.20
    else:
        totalMor = 0
    total = totalMac + totalMor
    if (total > 25):
        desc = total*0.10
        totalDesc = total - desc
    else:
        totalDesc = total

    return(SAIDA.format(totalMac=x, ValorMac=totalMac, totalMor=y, ValorMor=totalMor, total=total, totalDesc=totalDesc))

def main():
    try:
        maca = float(input("Digite a quantidade de macas: "))
        morango = float(input("Digite a quantidade de morangos: "))
        print(calculo(maca, morango))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
