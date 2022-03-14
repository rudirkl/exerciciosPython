#!/usr/bin/python3

def main():
    nome = str(input("Digite seu nome: ").upper())
    inverso = nome[::-1]
    print('Nome: {}\nInverso:{} '.format(nome, inverso))

if __name__ == "__main__":
    main()
