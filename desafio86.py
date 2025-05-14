lista = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]

for i in range(len(lista)):
    for j in range(len(lista[i])):  # Corrigido para iterar sobre a sublista
        n = int(input(f"Digite valores para {i},{j}: "))
        lista[i][j].append(n)  # Adiciona o valor à sublista

print(lista[0])  # Exibe a lista preenchida
print(lista[1])  # Exibe a lista preenchida
print(lista[2])  # Exibe a lista preenchida

