#!/usr/bin/python3

def area(x: float) -> float:
    pi = 3.14
    return (pi*x**2) # pi x raio ao quadrado

def main():
    raio = float(input("Digite o raio do circulo= "))
    print('a area do circulo e: {} '.format(area(raio)))

if __name__=="__main__":
    main()

