#!/usr/bin/python3

def calculo():
    i = 0
    ult = 1
    pen = 0
    mem = []
    while (i <= 500):
        if(i==0):
            mem.append(i)
            mem.append(1)
        i = ult + pen
        pen = ult
        ult = i
        mem.append(i)
    return(mem)

def main():
    print(calculo())

if __name__ == "__main__":
    main()
