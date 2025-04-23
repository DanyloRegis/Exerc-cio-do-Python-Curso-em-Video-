from math import factorial

# Atividade 03 - Calcular o fatorial de um número

resposta = input("Deseja calcular o fatorial de um número? (Y/n)")   

if resposta.lower() == 'Y' or resposta.lower() == 'y' :
    numero = int(input("Digite um numero inteiro positivo "))
    fatorial = factorial(numero)
    print(f"O fatorial de {numero} e: {fatorial}")
else:
    print("Vc escolhe nao calcular o fatorial")  