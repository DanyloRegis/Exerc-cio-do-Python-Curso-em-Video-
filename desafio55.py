mairor = 0
menor = 0
for i in range(3):
    n = int(input("Digite seu peso da {i} pesoa: "))
    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"O maior peso é {maior} e o menor peso é {menor}.")
