#!/usr/bin/python3

def main():
    print("Loja quase dois - Tabela de precos")
    for i in range(1,51):
        val = 1.99*i
        print(f"{i} - R${val:.2f}")

if __name__ == "__main__":
    main()
