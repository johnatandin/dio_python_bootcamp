#PROGRAMACAO ORIENTADA A OBJETOS
#em python se utiliza self em vez de this para referenciar os atributos.

class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor
        
    def buzinar(self):
        print("PlimPLIM")
    def parar(self):
        print("Parando a bicicleta../")
        print("Bicicleta parada..")
    def correr(self):
        print("correndooo....")
    
    #acessando os metodos e nome da classe e exibindo em forma de dicionario
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Branca","Caloi",2024,600)

b1.buzinar()
b1.parar()
b1.correr()

#print(b1.cor,b1.modelo,b1.ano,b1.valor)

print(b1)



