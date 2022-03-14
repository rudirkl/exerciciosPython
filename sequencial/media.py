#!/usr/bin/python3

def media(num1: float, num2: float, num3: float, num4: float) -> float:
    return ((num1 + num2 + num3 + num4) / 4) 

def main():
    num1 = float(input("Digite o primeiro numero= "))
    num2 = float(input("Digite o segundo numero= "))
    num3 = float(input("Digite o segundo numero= "))
    num4 = float(input("Digite o segundo numero= "))
    
    print( media(num1, num2, num3, num4))
    

if __name__=="__main__":
    main()
