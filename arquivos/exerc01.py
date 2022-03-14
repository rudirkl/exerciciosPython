#!/usr/bin/python3

arq = open("teste.txt", "r")

for linha in arq:
    val = linha.split()
    print(val)
