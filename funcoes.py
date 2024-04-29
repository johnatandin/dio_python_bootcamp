from unicodedata import numeric


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



def calcular_total(numero1 : int,numero2: int):
    return sum(numero1 ,numero2)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor , sucessor

calcular_total(5,5)
retorna_antecessor_e_sucessor(5)

    

#%% #objetos de primeira classe
def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operacao eh = {resultado}")
    
exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)
# %% escopo global e local
salario = 2000
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario
salario_bonus(100)

# %%
#Dado o código: 
def funcao(*args, **kw):
    

#qual será o valor de args e kw ao executar:
funcao("python", 2022, curso="dio")  # noqa: E999
# %%


    

    
 

# %%
