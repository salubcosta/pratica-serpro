//console.log('Hello, World!');
var x;      // is undefined
x = 5;      // is number
x = "John"; // is string

let nome = "Salumão";

var elementoP = document.getElementById('elementoP');
elementoP.innerHTML = nome; 

const numero = 50;

elementoP.innerHTML = numero > 50 ? "Maior" : "Menor";