from math import hypot
# Atividade 04 - Calcular a hipotenusa de um triângulo retângulo

x = float(input("Digite o valor do cateto oposto: "))
y = float(input("Digite o valor do cateto adjacente: "))

print("A hipotenusa é: ", hypot(x, y))