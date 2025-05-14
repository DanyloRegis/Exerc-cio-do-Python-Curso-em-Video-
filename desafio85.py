lista=[[],[]]

for i in range(7):
    n = int(input(f"digite o {i+1} numero "))
    if n % 2 == 0:
        lista[0].append(n)  # Adiciona ao índice 0 (pares)
    else:
        lista[1].append(n)
pares_formatados = ", ".join(map(str, lista[0]))
impares_formatados = ", ".join(map(str, lista[1]))
print(f"Números pares: {pares_formatados}")
print(f"Números ímpares: {impares_formatados}\n")