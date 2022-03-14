#!/usr/bin/python3

SAIDA = '''
tipo de pagamento = {cartao}
tipo de carne = {tipo}
desconto = {desconto:0.2f}
total = R${total:0.2f}
total a pagar = {totalDesc:0.2f}
'''

def calculo(x: int, y: float, z: int):
    
    if (x == 0 and y <= 5):
        tipo = "File duplo"
        total = 4.90*y
    elif (x == 0 and y > 5):
        tipo = "File duplo"
        total = 5.80*y
    elif (x == 1 and y <= 5):
        tipo = "Alcatra"
        total = 5.90*y
    elif (x == 1 and y > 5):
        tipo = "Alcatra"
        total = 6.80*y 
    elif (x == 2 and y <= 5):
        tipo = ""
        total = 6.90*y
    elif (x == 2 and y > 5):
        total = 7.80*y
    else:
        return("Valor invalido")
    if (z == 0):
        cartao = "sem cartao"
        desc = 0
        totalDesc = total
        return(SAIDA.format(tipo=tipo, total=total, cartao=cartao, desconto=desc, totalDesc=totalDesc))
    else:
        cartao = "com cartao"
        desc = total*0.05
        totalDesc = total - desc
        return(SAIDA.format(tipo=tipo, total=total, cartao=cartao, desconto=desc, totalDesc=totalDesc))

def main():
    try:
        tipo = int(input(''' 
Digite o tipo de carne
0 = File duplo
1 = Alcatra
2 = Picanha
--> '''))
        qnt = float(input("\nDigite a quantidade: "))
        cartao = int(input('''
Digite 1 se tiver cartao de desconto ou 0 se nao tiver: '''))
        print(calculo(tipo,qnt,cartao))
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
