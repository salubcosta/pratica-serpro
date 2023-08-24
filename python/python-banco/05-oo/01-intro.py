class aeronave():
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def utilizarFlaps(self):
        pass
    
    def movimentarTP(self, command):
        if command == 1:
            return "Baixando TREM DE POUSO"
        else:
            return "Recolhendo TREM DE POUSO"
    
    def acelerar(self):
        pass

cessna = aeronave("Cessna", 1960, "Branco")
print(cessna.modelo)
print(cessna.movimentarTP(1))