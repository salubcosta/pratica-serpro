carro = {"marca": "Ford", "modelo": "Mustang", "ano": 2023}

print("Marca: " +   carro["marca"])
print("Modelo: " +  carro.get("modelo"))
print("Ano: " +     str(carro["ano"]))

carros = {"carro1": carro,"carro2": dict(carro)} # o dict cria novo dicionário sem referência

carros["carro2"]["modelo"] = "Territory"
print(carros["carro2"]["modelo"])
print(carros)
del carros["carro1"]
print(carros)