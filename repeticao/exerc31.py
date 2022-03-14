#!/usr/bin/python3

PROD = []

def calculo(x: int):
    soma = 0
    din = float(input("Digite o valor em dinheiro: "))
    print("Lojas tabajara")
    for i in range(x):
        soma += PROD[i]
        print(f"Produto {i}: R${PROD[i]}")
    troco = din - soma
    print(f"Total: R${soma}\nDinheiro: R${din}\nTroco: R${troco}")

def main():
    val = True
    while (val):
        num = float(input("Digite uma valor ou 0 para sair:  "))
        if(num == 0):
            val = False
        else:
            PROD.append(num)
    tam = len(PROD)
    calculo(tam)

if __name__ == "__main__":
    main()
