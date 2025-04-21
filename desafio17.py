import math

def hipotenusa(cateto_oposto, cateto_adjacente):
    # Calcula a hipotenusa usando o Teorema de Pitágoras
    return math.sqrt(pow(cateto_adjacente, 2) + pow(cateto_oposto, 2))

# Solicita ao usuário os valores dos catetos
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

# Chama a função para calcular a hipotenusa
resultado = hipotenusa(cateto_oposto, cateto_adjacente)

# Exibe o resultado
print(f"A hipotenusa é {resultado:.2f}")
