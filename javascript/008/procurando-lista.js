const alunos = ["João", "Maria", "Bia", "Fernanda"];

const buscarAluno = (nome, lista)=>{
    for(var i=0; i < lista.length; i++){
        if(lista[i] == nome){
            return lista[i];
        }
    }
    return "Aluno não encontrado!";
}

console.log(buscarAluno("Bia", alunos));