#!/usr/bin/python3

SAIDA = '''
Nome = {nome}
Idade = {idade}
Salario = {salario}
Sexo = {sexo}
Estado civil = {estado}
'''

def calculo(nome: str, idade: int, sal: float, sex: str, est: str, cont: int):
    x = len(nome)
    sex = sex.lower()
    f = "f"
    m = "m"
    print(sex)
    est = est.lower()
    if(x <=3):
        return("Nome deve ser maior que 3 caracteres.\n",cont)
    elif(idade < 0 and idade >150):
        return("Idade deve ser entre 0 e 150.\n",cont)
    elif(sal <= 0):
        return("Salario deve ser maior que 0.\n",cont)
    elif(sex not in('f','m')):
        return("Sexo deve ser f ou m.\n",cont)
    elif(est not in('s','c','v','d')):
        return("Estado civil deve ser s, c, v ou d.\n",cont)
    else:
        cont = 1
        result = SAIDA.format(nome=nome,idade=idade,salario=sal,sexo=sex,estado=est)
        return(result,cont)

def main():
    try:
        cont = 0
        while(cont == 0):
            nome = str(input("Digite seu nome: "))
            idade = int(input("Digite a sua idade: "))
            salario = float(input("Digite seu salario: "))
            sexo = str(input("Digite o sexo, m->masculino ou f->feminino: "))
            estado = str(input('''
Digite o estad civil:
s -> solteiro
c -> casadp
v -> viuvo
d -> divorciado
: '''))
            result,cont = (calculo(nome, idade, salario, sexo, estado, cont))
            print(result)
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
