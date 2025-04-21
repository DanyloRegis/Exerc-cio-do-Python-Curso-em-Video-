from math import ceil, floor

def mudar_numero(valor):
    
    valor = valor.replace(",", ".")  
    return float(valor)

numero = input("Digite um número: ")
numero = mudar_numero(str(numero))
arredondado_cima = ceil(numero)
arredondado_baixo = floor(numero)
print(f"A o numero arendodado para baixo e {arredondado_baixo} e para cimia {arredondado_cima}")