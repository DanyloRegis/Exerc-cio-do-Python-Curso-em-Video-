import math

angulo = float(input("Digite o valor do ângulo em graus: "))
raiz = math.radians(angulo)
print(f"O seno de {angulo} graus é: {math.sin(raiz):.2f}")
print(f"A tangente de {angulo} graus é: {math.tan(raiz):.2f}")