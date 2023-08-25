# def add(a, b):
#     return a + b



# def soma(a, b):
#     return a + b
# import re

# def validar_email(email):  
#     padrao = r'^[\w\.-]+@[\w\.-]+\.\w+s
#     return re.match(padrao, email) is not None

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

def calcular_media(lista_numeros):
    total_numeros = len(lista_numeros)
    
    if total_numeros == 0:
        return 0
    
    soma = sum(lista_numeros)
    return soma / total_numeros