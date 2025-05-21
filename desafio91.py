import random
import time
from operator import itemgetter

# Initialize the players' scores
lista = {
    "jogador1": [],
    "jogador2": [],
    "jogador3": [],
    "jogador4": [],
}

# Roll the dice for each player
for i, jogador in enumerate(lista.keys(), start=1):
    resultado = random.randint(1, 6)
    lista[jogador].append(resultado)
    print(f"O jogador {i} tirou {resultado}")
    time.sleep(0.5)

# Sort the players based on their scores
top = sorted(lista.items(), key=itemgetter(1), reverse=True)

# Display the sorted results
print("\nRanking dos jogadores:")
for i, (jogador, resultados) in enumerate(top, start=1):
    print(f"{i}. {jogador} com resultado {resultados[0]}")
