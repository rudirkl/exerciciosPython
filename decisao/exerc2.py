#!/usr/bin/python3

def valor(x: float):
    if (x > 0):
        res = "o numero e positivo"
    elif(x<0):
        res = "os numero e negativo"
    else:
        res = "e zero"
    return (res)


def main():
    num1 = float(input("Digite o primeiro numero: "))
    print(valor(num1))

if __name__ == "__main__":
    main()
