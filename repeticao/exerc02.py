#!/usr/bin/python3

def calculo(x: str, y: str, z: int):
    if (x != y):
        z = 1
    else:
        print("\nusuario e senha nao podem ser os mesmos\n")
    return(x,y,z)

def main():
    try:
        cont = 0
        while(cont == 0):
            user = str(input("Digite o nome de usuario: "))
            senha = str(input("Digite a senha: "))
            user, senha, cont = calculo(user,senha, cont)
        print("\nUsuario: "+user+"\nSenha: "+senha)
    except:
        print("Algo deu errado")

if __name__ == "__main__":
    main()
