var produtos = document.getElementById("produtos");

var objProdutos = [
    {
        nome: "Teclado",
        preco: 189.9
    },{
        nome: "SSD 1TB",
        preco: 659.99
    }
];

for(var x = 0; x < objProdutos.length; x++){
    var produtoItem = document.createElement("p");
    produtoItem.innerHTML = `${objProdutos[x].nome} - Preço: R$ ${objProdutos[x].preco}`;
    produtos.appendChild(produtoItem);
}