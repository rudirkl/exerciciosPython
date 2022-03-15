#!/usr/bin/python3

def palindromo(x: str):
    x = x.casefold()
    inv = x[::-1]
    if(x == inv):
        return("E palindromo")
    else:
        return("Nao e palindromo")

def main():
    frase = str(input("Digite a palavra ou frase: "))
    print(palindromo(frase))

if __name__ == "__main__":
    main()
