#!/usr/bin/python3

def media(x: int, y: int, z: float) -> float:
    r1 = (x*2) * (y/2) # o produto do dobro do primeiro com metada do segundo
    r2 = (y*3) + z # a soma do triplo do primeiro com o terceiro
    r3 = z**3 # o terceiro elevado ao cubo
    return (r1,r2,r3)

def main():
    num1 = int(input("Digite o primeiro numero= "))
    num2 = int(input("Digite o segundo numero= "))
    num3 = float(input("Digite o segundo numero= "))
    
    print( media(num1, num2, num3))
    

if __name__=="__main__":
    main()

