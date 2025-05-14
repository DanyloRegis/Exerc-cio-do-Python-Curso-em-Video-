import random

lista = random.sample(range(1, 100), 10)  # Gera uma lista de 10 números aleatórios entre 1 e 100
maior = max(lista)  # Encontra o maior número da lista
menor = min(lista)  # Encontra o menor número da lista

print("Lista:", ", ".join(map(str, lista)))  # Converte números para strings e junta com vírgulas
print("Maior número:", maior)  # Imprime o maior número 
print("Menor número:", menor)  # Imprime o menor número


