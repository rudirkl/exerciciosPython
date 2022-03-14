#!/usr/bin/python3

def celsius(x: float) -> float:
    return (((x*9)/5)+32)

def main():
    c = float(input("Digite a temperatura em celsius = "))
    print('a temperatura em fahrenheit e: {} '.format(celsius(c)))

if __name__=="__main__":
    main()

