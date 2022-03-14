#!/usr/bin/python3

def total(x: float):
    if (x <= 280):
        rej = x * 0.20
        novo = x + rej
        return(x, novo, "20%", rej)
    elif (x > 280 and x < 700):
        rej = x * 0.15
        novo = x + rej
        return(x, novo, "15%", rej)
    elif (x > 700 and x < 1500):
        rej = x * 0.10
        novo = x + rej
        return(x, novo, "10%", rej)
    elif (x >= 1500):
        rej = x * 0.05
        novo = x + rej
        return(x, novo, "5%", rej)
    else:
        return("invalido")

def main():
    salario = float(input("Digite o valor do salario: "))
    print(total(salario))
    

if __name__ == "__main__":
    main()
