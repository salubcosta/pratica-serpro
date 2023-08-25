const mysql = require('mysql2/promise');

// Configuração de conexão
const config = {
    host: 'localhost',
    user: 'root',
    password: 'senha',
    database: 'python_udemy'
};

// Função para executar uma consulta SQL
async function executeQuery(sql, values = []){
    const connection = await mysql.createConnection(config);
    const [results] = await connection.execute(sql, values);
    connection.end();
    return results;
}

// Inserir novo usuário
async function createaluno(nome, email, status){
    try {
        const sql = 'INSERT INTO ALUNOS (nome, email, status) VALUES (?,?,?)';
        await executeQuery(sql, [nome, email, status])
        console.log('Aluno cadastrado com sucesso!')
    } catch(error){
        console.error('Falha ao cadastrar novo aluno!', error)
    }
}

async function readAlunos(){
    try {
        const sql = 'SELECT * FROM alunos';
        const alunos = await executeQuery(sql)
        alunos.forEach(aluno => console.log(aluno));
    } catch(error) {
        console.error('Falha ao buscar alunos!'. error)
    }
}

async function updateAluno(id, nome, email, status){
    try{
        const sql = 'UPDATE ALUNOS SET NOME=?, EMAIL=?, STATUS=? WHERE ID=?;';
        await executeQuery(sql, [nome, email, status, id])
        console.log('Aluno atualizado com sucesso!')
    }catch(error){
        console.error('Falha ao atualizar aluno!', error)
    }
}

async function deleteAluno(id){
    try {
        const sql = 'DELETE FROM ALUNOS WHERE ID=?'
        await executeQuery(sql, [id])
        console.log('Aluno deletado com sucesso!')
    } catch(error){
        console.error('Falha ao deletar aluno!', error)
    }
}

//readAlunos();
//createaluno('Joelda Francisca', 'joeldabcosta@gmail.com', 1)
//readAlunos();
//updateAluno(2, 'Carla Lee Sa', 'carla.lee@mail.com', 1)
//readAlunos();
//deleteAluno(2)
readAlunos();
