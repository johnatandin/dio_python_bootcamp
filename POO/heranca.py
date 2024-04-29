class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa= placa
        self.numero_rodas = numero_rodas
    def ligar_motor(self):
        print("Ligando o motor")
        
        

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__():
        


moto = Motocicleta("preta","123-Z34", 2)
moto.ligar_motor()

carro = Carro("azul","abc-123",4)
carro.ligar_motor()

caminhao = Caminhao("roxo","gdf-232", 8)
caminhao.ligar_motor()


