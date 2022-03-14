#!/usr/bin/python3

SAIDA = '''
Fatorial de: {fatorial}
{fatorial}! = {dese} = {res}
'''

def calculo(x: int):
    res = 1
    dese = ""
    for i in range(x,0,-1):
        if(i==x):
            dese += str(f"{i}")
            res *= i
        else:
            dese += str(f".{i}")
            res *= i
    print(SAIDA.format(fatorial=x,dese=dese,res=res))
    
def main():
    num = int(input("Digite um numero: "))
    calculo(num)

if __name__ == "__main__":
    main()
