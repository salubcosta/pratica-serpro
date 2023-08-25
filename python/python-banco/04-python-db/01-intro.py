import pymysql.cursors

def getConn():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="senha",
            db="PYTHON_UDEMY",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except:
        print("Falha ao conectar com o banco de dados!")

def selectAll():
    try:
        with getConn().cursor() as cursor:
            cursor.execute("SELECT * FROM alunos")
            result = cursor.fetchall()
            return result
    except:
        print("Falha ao realizar a consulta")

def addAluno(conn):
    print("Adicionando Alunos")
    nome = input("Informe seu nome: ")
    email= input("Informe seu e-mail: ")
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO ALUNOS (nome, email, status) VALUES (%s, %s, 1)"
            cursor.execute(sql, (nome, email))
        conn.commit()
        print("Aluno cadastrado com sucesso!")
    except:
         print("FALHA ao cadastrar novo aluno!")

def updateAluno(conn):
    id = input("Infome o ID: ")
    if len(id) == 0:
        return
    nome = input("Novo nome: ")
    email = input("Informe novo e-mail: ")
    status = input("Informe novo status: ")
    sql = "UPDATE ALUNOS SET "
    sql += f" nome='{nome.strip()}', " if nome.strip() != "" else " nome=nome,"
    sql += f" email='{email.strip()}', " if email.strip() != ""  else " email=email, "
    sql += f" status='{status.strip()}' " if status.strip() != "" else " status=status"
    sql += f" where id={id}"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit();
    except:
        print("Falha ao realizar update!")
    
def deleteAluno(id):
    conn = getConn()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM alunos where ID=%s",(id))
        conn.commit()
        print("Registro de aluno excluído com sucesso!")
    except:
        print("Falha ao excluir registro")

#print(f"Usuário: [{id}] - Novos dados para nome: {nome}. E-mail: {email}. Status: {status}")
#print(sql)

#addAluno(getConn())
#updateAluno(getConn())
deleteAluno(15)
#for i in selectAll():
#    print(i['NOME'])

