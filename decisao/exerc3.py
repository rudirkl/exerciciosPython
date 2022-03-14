#!/usr/bin/python3

def maior(x: str):
    if (x == "F"):
        res = "Feminino"
    elif ( x == "M"):
        res = "Masculino"
    else:
        res = "invalido"
    return (res)


def main():
    num1 = str(input("Digite F para feminino ou M para masculino: "))
    print(maior(num1))

if __name__ == "__main__":
    main()
