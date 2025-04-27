import random

# Desafio 28 - Jogo da Adivinhação  

n = random.randint(1, 5)  # Número aleatório entre 1 e 5

print("vamos jogar um jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 5")

tentativas = int(input("Quantas tentativas você quer? "))

if tentativas == n:
    print("Parabéns! Você adivinhou o número!")
else:
    print("Você não adivinhou o número. Tente novamente!")
    print(f"O número era {n}.")
    print("Fim do jogo.")