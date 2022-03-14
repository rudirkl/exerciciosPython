#!/usr/bin/python3

def main():
    print("Panificadora pao de ontem - Tabela de precos")
    for i in range(1,51):
        val = 0.18*i
        print(f"{i} - R${val:.2f}")

if __name__ == "__main__":
    main()
