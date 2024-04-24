# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

def recomendar_plano(consumo):
  
  if(consumo <=10):
    return "Plano Essencial Fibra - 50Mbps"
  
  elif(consumo >10 and consumo <=20):  
    return "Plano Prata Fibra - 100Mbps"
  
  elif(consumo >20):
    return"Plano Premium Fibra - 300Mbps"
  
  

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))


# %%
# Módulo 're' que fornece operações com expressões regulares.
import re

# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
# TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
def validate_numero_telefone(phone_number):
    padrao = r'\(\d{2}\) 9\d{4}-\d{4}'
    correspondencia = re.fullmatch(padrao, phone_number)
    return correspondencia is not None

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)
# %%
import re

# Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    # Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    padrao = r'\(\d{2}\) 9\d{4}-\d{4}'
    
    # A função 're.match()' verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(padrao, phone_number):  
        # Agora crie um return, para retornar que o número de telefone é válido:
        return "Número de telefone válido."
    else:
        # Crie um else e return, caso o número de telefone seja inválido:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input("Por favor, insira um número de telefone: ")  

# Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)
# %%
