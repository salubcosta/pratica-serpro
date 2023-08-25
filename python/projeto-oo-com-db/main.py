import admin as adm

def main():
    print("Escolha:\n1 - Logar como Administrador\n2 - Cadastrar Usuário\n3 - Ver Catálogo\n0 - Sair ")
    op = int(input("Informe sua escolha: "))
    if op == 1:
        adm.admin().login()
    elif op == 2:
        adm.admin().cadastrar()
    elif op ==3:
        pass
    else:
        pass

if __name__ == "__main__":
    main()