#Com base no exercício no qual você utilizou o método split(). 
#Crie uma função chamada retornaDominio que retorne o domínio de um email. Por exemplo, email = 'fulano@dominio.com'
#Sua função deve retornar: 'dominio.com'
#Lembre-se que no método split() você pode passar por parâmetro onde quer serparar uma string em uma lista.
def retornaDominio(email):
    return email.split("@")[1]
print(retornaDominio("meu.email@gmail.com"))