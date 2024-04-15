def exibir_mensagem():
    print("Ola Mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    
    
def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()

exibir_mensagem_2(nome="Johnatan")
exibir_mensagem_3()
exibir_mensagem_3(nome="Testando")



def calcular_total(numero1,numero2):
    return sum(numero1,numero2)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor , sucessor

calcular_total()
retorna_antecessor_e_sucessor(5)

    

