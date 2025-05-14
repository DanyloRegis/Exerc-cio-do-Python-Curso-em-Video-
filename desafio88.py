import random
lista = []
num_listas_vazias = int(input("Quantas vezes vc vai jogar? "))

for i in range(num_listas_vazias):
# Cria a lista com a estrutura desejada
    lista = [[random.randint(1, 100) for _ in range(6)]]
    formatados = ", ".join(map(str, lista))
    print(f"jogo {i+1}: {formatados}")