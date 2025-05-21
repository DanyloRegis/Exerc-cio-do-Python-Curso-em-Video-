lista = {
    "jogador": [],
    "jogos": [],
    "total": []
}

gols =[]

soma=0

# Adiciona um jogador
nome = str(input("Nome do jogador: "))
lista["jogador"].append(nome)

partida = int(input("numero de jogos "))

for i in range(partida):
    gols.append(int(input(f"Número de gols na partida {i + 1}: ")))

lista["jogos"]= gols[:]
lista["total"] = sum(gols)
print(lista)

for a,b in  lista.items():
    print(f"O campo o {a} recebe o valor {b} ")
    
print(f"O jodador: {lista["jogador"]} partidipou de {len(lista["jogos"])}")

for n,m in enumerate(lista["jogos"]):
    print(f"na paratida {n+1} o jogador marcou {m}")

