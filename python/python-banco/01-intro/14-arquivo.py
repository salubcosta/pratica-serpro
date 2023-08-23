"""
w - escrever
a - alterar
r - ler
"""
def criarArquivo():
    file = open("python/python-banco/teste-arquivo.txt", "w")
    file.write("era uma vez")
    file.close()
def lerArquivo():
    file = open("python/python-banco/teste-arquivo.txt", "r")
    print(file.readline())
    file.close()

# criar arquivo
#criarArquivo()
lerArquivo()