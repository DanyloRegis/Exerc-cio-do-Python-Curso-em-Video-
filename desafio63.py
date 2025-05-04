fibonati = int(input("Digite o número de termos da sequência de Fibonacci: "))

while fibonati <= 0:
    print("Número inválido! Tente novamente.")
    fibonati = int(input("Digite o número de termos da sequência de Fibonacci: "))

x, y = 0, 1  # Corrigido: Fibonacci começa em 0, 1
contador = 0

while contador < fibonati:
    print(x, end=" ➤ ")  # Imprime o termo atual
    x, y = y, x + y      # Atualiza os valores corretamente
    contador += 1

print("FIM")