#!/usr/bin/python3

def tempo(x: float, y: float):
    velMB = y/8
    tempoAprox = x/velMB
    minutos = int(tempoAprox/60)
    segundos = tempoAprox%60
    return("Tempo para download: "+str(minutos)+" minutos e "+str(segundos)+" segundos")

def main():
    tam = float(input("digite o tamanho do arquivo em MB"))
    vel = float(input("digite a velocidade do link em Mbps"))
    print(tempo(tam, vel))

if __name__ == "__main__":
    main()
