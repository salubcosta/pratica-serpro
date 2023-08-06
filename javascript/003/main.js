function calcularAutonomia(){
    var consumo = document.getElementById('consumo').value;
    var valorLitro = document.getElementById('valor-litro').value;
    var abastecimento = document.getElementById('abastecimento').value;
    var resultado = document.getElementById('resultado');

    let autonomia = parseFloat(abastecimento)/parseFloat(valorLitro) * parseFloat(consumo);

    resultado.innerText = `Autonomia será de: ${autonomia.toFixed(2).toString()} KM de distância`;
}

var clientes = [
    {cpf: '111', nome: 'Bia', profissao: 'AD', renda: 14000},
    {cpf: '222', nome: 'Zaza', profissao: 'DBA', renda: 25000},
    {cpf: '333', nome: 'Salumao', profissao: 'DEV', renda: 20000}
];

function buscarCliente(entrada){
    var cpf = entrada.value;
    for(var x = 0; x < clientes.length; x++){
        if(cpf == clientes[x].cpf){
            document.getElementById('nome').value = clientes[x].nome;
            document.getElementById('profissao').value = clientes[x].profissao;
            document.getElementById('renda').value = clientes[x].renda;
        }
    }
}