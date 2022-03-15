#!/usr/bin/python3

def funcao(x: str):
    contEsp = x.count(" ")
    vogals = 'aeiou'
    x = x.casefold()
    vogCount = dict.fromkeys(vogals, 0)
    for i in x:
        if i in vogCount:
            vogCount[i] += 1 
    return(vogCount, contEsp)

def main():
    frase = str(input("Digite a frase: "))
    print(funcao(frase))


if __name__ == "__main__":
    main()
