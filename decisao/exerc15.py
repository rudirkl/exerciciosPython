#!/usr/bin/python3

def triangulo(x: float, y:float, z: float):
    if ((x+y < z) or (x+z < y) or (y+z < x)):
        return("Nao e triangulo")
    else:   
        if (x==y and x==z):
            return("triangulo equilatero")
        elif (x==y or x==z or z==y):
            return("trianulo isoceles")
        elif (x!=y and x!=z and y!=z):
            return("triangulo escaleno")

def main():
    try:
        lado1 = float(input("Digite o lado 1: ")) 
        lado2 = float(input("Digite o lado 2: "))
        lado3 = float(input("Digite o lado 3: "))
        
        print(triangulo(lado1,lado2,lado3))

    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
