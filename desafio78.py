lista = []
for i in range(5):
    lista.append(int(input(f"Digite um número para a posicao {len(lista)}: ")))
    
posicoes = {}

for i, c in enumerate(lista):
    if c in posicoes:
        posicoes[c].append(i)
    else:
        posicoes[c] = [i]

# Encontrar o menor e o maior valor
menor = min(lista)
maior = max(lista)

# Imprimindo as posições do menor valor
if menor in posicoes:
    posicoes_menor_str = ', '.join(map(str, posicoes[menor]))
    print(f"Na posição {posicoes_menor_str} temos o menor valor {menor}.")

# Imprimindo as posições do maior valor
if maior in posicoes:
    posicoes_maior_str = ', '.join(map(str, posicoes[maior]))
    print(f"Na posição {posicoes_maior_str} temos o maior valor {maior}.")
