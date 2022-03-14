#!/usr/bin/python3

CONS = ['a','e','i','o','u']

def maior(x: str):
    for y in CONS:
        if (x == y):
            res = "vogal"
            break
        else:
            res = "consoante"
    print(res)



def main():
    num1 = str(input("Digite uma letra: "))
    num1.lower()
    (maior(num1))

if __name__ == "__main__":
    main()
