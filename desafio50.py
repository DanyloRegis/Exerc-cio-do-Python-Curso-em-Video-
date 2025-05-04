soma = 0
for i in range(0, 6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        cont = cont + 1
        soma += n
print(f"A soma de todos os {cont} números pares é: {soma}")