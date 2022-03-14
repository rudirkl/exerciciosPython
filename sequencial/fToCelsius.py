#!/usr/bin/python3

def celsius(x: float) -> float:
    return (5*((x-32)/9))

def main():
    f = float(input("Digite a temperatura em fahreneit= "))
    print('a temperatura e: {} '.format(celsius(f)))

if __name__=="__main__":
    main()
