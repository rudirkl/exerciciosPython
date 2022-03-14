#!/usr/bin/python3

def area(x: float) -> float:
    return (x**2) # pi x raio ao quadrado

def main():
    lado = float(input("Digite o valor do lado do quadrado= "))
    print('a area do circulo e: {} '.format(area(lado)))

if __name__=="__main__":
    main()
