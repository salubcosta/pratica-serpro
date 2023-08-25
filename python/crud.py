import mysql.connector 

def getConnection():
    config = {
        "user": "root",
        "password": "senha",
        "host": "localhost",
        "database": "python_udemy"
    }
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(f"Falha ao realizar a conexão com banco de dados. Error: {err}")

def create_aluno(conn, nome, email, status):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO ALUNOS (NOME,EMAIL,STATUS)VALUES(%s,%s,%s);"
            cursor.execute(sql, (nome,email,status))
        conn.commit()
        print("Aluno cadastrado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Falha ao cadastrar novo aluno! Error: {err}")

def read_alunos(conn):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM alunos"
            cursor.execute(sql)
            alunos = cursor.fetchall()
            for aluno in alunos:
                print(aluno)
    except mysql.connector.Error as err:
        print(f"Falha ao buscar alunos! Error: {err}")

def update_aluno(conn, nome, email, status, id):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE ALUNOS SET NOME=%s, EMAIL=%s, STATUS=%s WHERE ID=%s;"
            cursor.execute(sql, (nome, email, status, id))
        conn.commit()
        print("Aluno atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Falha ao atualizar aluno! Error: {err}")

def delete_aluno(conn, id):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM ALUNOS WHERE ID=%s;"
            cursor.execute(sql, (id,))
        conn.commit()
        print("Aluno deletado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Falha ao deletar aluno. Error: {err}")

try:
    connection = getConnection()
    #create_aluno(connection, "Bianca Braga", "biancab@hotmail.com", 1)
    read_alunos(connection)
    update_aluno(connection, "Beatriz Borges", "beatrizbborges@gmail.com",0,16)
    read_alunos(connection)
    #delete_aluno(connection, 3)
    #read_alunos(connection)
except mysql.connector.Error as err:
    print(f"Falha ao realizar operação! Error: {err}")
finally:
    if connection.is_connected():
        connection.close()