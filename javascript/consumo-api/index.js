const axios = require("axios");

const apiUrl = "https://jsonplaceholder.typicode.com/posts/1";

axios.get(apiUrl)
    .then(response =>{
        console.log('Dados da API: ', response.data)
    }).catch(error=>{
        console.error('Erro ao consumir a API: ', error)
    });

    

