#!/usr/bin/python3

def total(x: float, y: float):
    return (x * y)

def calculo(x: float):
    if (x <= 900):
        inss = x * 0.10
        fgts = x * 0.11
        totalDesc = inss
        liquido = x - inss
        saida = '''
        Salario bruto        : R${x}
        IR                   : isento
        INSS                 : R${inss}
        FGTS                 : R${fgts}
        Total de descontos   : R${totalDesc}
        Salario liquido      : R${liquido}
                '''
        return(saida.format(x=x, inss=inss, fgts=fgts, liquido=liquido, totalDesc=totalDesc))

    elif (x > 900 and x <= 1500):
        ir = x * 0.05
        inss = x * 0.10
        fgts = x * 0.11
        totalDesc = inss + ir
        liquido = x - (inss + ir)
        saida = '''
        Salario bruto        : R${x}
        IR                   : R${ir}
        INSS                 : R${inss}
        FGTS                 : R${fgts}
        Total de descontos   : R${totalDesc}
        Salario liquido      : R${liquido}
                '''
        return(saida.format(x=x, ir=ir, inss=inss, fgts=fgts, liquido=liquido, totalDesc=totalDesc))
       
    elif (x > 1500 and x <= 2500):
        ir = x * 0.05
        inss = x * 0.10
        fgts = x * 0.11
        totalDesc = inss + ir
        liquido = x - (inss + ir)
        saida = '''
        Salario bruto        : R${x}
        IR                   : R${ir}
        INSS                 : R${inss}
        FGTS                 : R${fgts}
        Total de descontos   : R${totalDesc}
        Salario liquido      : R${liquido}
                '''
        return(saida.format(x=x, ir=ir, inss=inss, fgts=fgts, liquido=liquido, totalDesc=totalDesc))

         
    elif (x > 2500):
        ir = x * 0.10
        inss = x * 0.10
        fgts = x * 0.11
        totalDesc = inss + ir
        liquido = x - (inss + ir)
        saida = '''
        Salario bruto        : R${x}
        IR                   : R${ir}
        INSS                 : R${inss}
        FGTS                 : R${fgts}
        Total de descontos   : R${totalDesc}
        Salario liquido      : R${liquido}
                '''
        return(saida.format(x=x, ir=ir, inss=inss, fgts=fgts, liquido=liquido, totalDesc=totalDesc))
        
    else:
        return("invalido")
         


def main():
    valHora = float(input("Digite  valor da hora: "))
    horas = float(input("Digite a quantidade de horas: "))
    
    valTotal = total(valHora, horas)

    print(calculo(valTotal))

if __name__ == "__main__":
    main()
