#!/usr/bin/python3

def main():
    nome = str(input("Digite seu nome: ").upper())
    for i in range(0,len(nome)+1):
        print(str(nome[:i]))

if __name__ == "__main__":
    main()
