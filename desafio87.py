lista = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]
maior = soma_pares = 0

for i in range(len(lista)):
    for j in range(len(lista[i])):
        n = int(input(f"Digite valores para {i},{j}: "))
        lista[i][j].append(n)
        if n % 2 == 0:
            soma_pares += n

# Encontrar o maior valor da terceira linha (índice 2)
maior_terceira_linha = max([item[0] for item in lista[2]])

# Soma dos valores da terceira linha
soma_terceira_coluna = sum(linha[2][0] for linha in lista)

print(lista[0])
print(lista[1])
print(lista[2])

print(f"Soma dos pares: {soma_pares}")
print(f"Maior valor da terceira linha: {maior_terceira_linha}")
print(f"Soma da terceira coluna: {soma_terceira_coluna}")



