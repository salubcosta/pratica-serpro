controle = 10
lista = [int(input("Informe um valor: ")) for i in range(controle)]
maior = 0
for i in lista:    
    if(int(i) > maior):
        maior = i;
print(f"O maior valor informado é: {maior}")