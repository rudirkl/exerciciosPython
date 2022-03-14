#!/usr/bin/python3

def maior(x: float, y: float):
    calculo = (x+y)/2
    if (calculo >= 7 and calculo < 10):
        res = "aprovado"
    elif ( x == 10):
        res = "aprovado com distincao"
    else:
        res = "reprovado"
    return (res)


def main():
    num1 = float(input("Digite a primeira nota: "))
    num2 = float(input("Digite a segunda nota: "))
    print(maior(num1, num2))

if __name__ == "__main__":
    main()
