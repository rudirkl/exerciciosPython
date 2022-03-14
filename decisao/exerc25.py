#!/usr/bin/python3

def resposta(a: int, b: int, c: int, d: int, e: int):
    val = 0
    if(a == 1):
        val += 1
    elif(a == 0):
        val = val
    else:
        print("Valor invalido")
    if(b == 1):
        val += 1
    elif(b == 0):
        val = val
    else:
        print("Valor invalido")
    if(c == 1):
        val += 1
    elif(c == 0):
        val = val
    else:
        print("Valor invalido")
    if(d == 1):
        val += 1
    elif(d == 0):
        val = val
    else:
        print("Valor invalido")
    if(e == 1):
        val += 1
    elif(e == 0):
        val = val
    else:
        print("Valor invalido")

    if (val == 5):
        return("Assassino")
    elif (val >= 3 and val < 5):
        return("cumplice")
    elif(val==2):
        return("suspeito")
    else:
        return("tudo ok")

def main():

    print('''
    Digite a opcao para cada perginta
    1 = SIM
    0 = NAo

    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e."Já trabalhou com a vítima?"
    ''')
    a = int(input("Resposta para letra A: "))
    b = int(input("Resposta para letra B: "))
    c = int(input("Resposta para letra C: "))
    d = int(input("Resposta para letra D: "))
    e = int(input("Resposta para letra E: "))

    print(resposta(a,b,c,d,e))

if __name__ == "__main__":
    main()
