import random

# Desafio 28 - Jogo da Adivinhação  
n = random.randint(1, 10)# Número aleatório entre 1 e 5
print("vamos jogar um jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 10")
tentativas_feitas = 0
while True:
    try:
        tentativas = int(input("Digite um número entre 1 e 10: "))

        if tentativas == n:
            tentativas_feitas += 1
            print(f"Parabéns! Você adivinhou o número! em {tentativas_feitas} tentativas.")
            if tentativas_feitas == 1:
                print("Você é muito sortudo!")
            print("Fim do jogo.")
            break
        elif tentativas > n:
            tentativas_feitas += 1
            print("Você errou! Numero maior que o esperado.")
            print("Tente novamente.")
        else:
            tentativas_feitas += 1
            print("Você errou! Numero menor que o esperado.")
            print("Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")
        continue