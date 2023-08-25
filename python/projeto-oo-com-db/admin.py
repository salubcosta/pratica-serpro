import mysql.connector

class admin():
    def __init__(self):
        pass

    def getConnection(self):
        try:
            config = {
                "user": "root",
                "password": "dbBar80%a$",
                "host": "localhost",
                "database": "projeto_aeronave"
            }
            self.conn = mysql.connector.connect(**config)
            print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro de conexão com o banco de dados. Error: {err}")

    def login(self):
        self.getConnection()
        email = input("Informe seu e-mail: ")
        password = input("Informe sua senha: ")
        authentication = False
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM tb_users")
                result = cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Falha ao realizar a autenticação. Error: {err}")
        for i in result:
            if email == i[2] and password == i[3]:
                authentication = True
                break
            else:
                pass
        if authentication:
            self.menuAdmin()
        else:
            print("Login inválido! Tente novamente!")
            self.login()

    def menuAdmin(self):
        print("\n1 - Cadastrar Aeronave\n2 - Alterar\n3 - Deletar\n4 - Listar\n0 - Sair!")
        op = int(input("Informe sua escolha: "))
        if op == 0:
            return 0
        elif op == 1:
            modelo = input("Informe modelo: ")
            ano = int(input("Informe ano: "))
            cor = input("Informe cor: ")
            tipo = int(input("Tipo (1.Avião|2.Helicóptero|3.Drone):  "))
            dadosAeronave = [modelo, ano, cor, tipo]
            aeronaves().cadastrarAeronave(dadosAeronave)
        elif op == 4:
            lista = aeronaves().listarAeronaves()
            for i in lista:
                print([i])

    def cadastrar(self):
        nome = input("Informe seu nome: ")
        email = input("Informe seu email: ")
        senha = input("Informe sua senha: ")
        status = input("Informe seu status: ")
        if self.verificarEmail(email) == 0:
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute("INSERT INTO TB_USERS (nome, email, senha, status) VALUES (%s, %s, %s, %s)", [nome, email, senha, status])
                    self.conn.commit()
                    print("Usuário cadastrado com sucesso!")
            except mysql.connector.Error as err:
                print(f"Falha ao realizar o cadastro. Error: {err}")
        else:
            print("Já existe esse e-mail cadastrado!")

    def verificarEmail(self, email):
        self.getConnection()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("select email from tb_users where email = %s",[email])
                result = cursor.fetchall()
                return len(result)
        except mysql.connector.Error as err:
            print(f"Falha ao verificar e-mail. Error: {err}")

class aeronaves(admin):
    def __init__(self):
        pass
    
    def cadastrarAeronave(self, dadosAeronave):
        self.getConnection()
        try:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO TB_AERONAVES (MODELO, ANO, COR, TIPO) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, dadosAeronave)
                self.conn.commit()
            print("Aeronave cadastrada com sucesso!")
            self.menuAdmin()
        except mysql.connector.Error as err:
            print(f"Erro ao realizar cadastro de aeronave! Error: {err}")
    
    def listarAeronaves(self):
        self.getConnection()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM tb_aeronaves")
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print(f"Falha ao listar aeronaves. Falha: {err}")