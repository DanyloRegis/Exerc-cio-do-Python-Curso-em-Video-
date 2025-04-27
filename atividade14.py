
import random

numero = random.randint(1, 100)
while True:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    tentativas = 0
    if tentativas != 5:
        if palpite < numero:
            tentativas = tentativas + 1
            print("Muito baixo! Tente novamente. ja foram {tentativas} tentativas.")
        elif palpite > numero:
            tentativas = tentativas + 1
            print(f"Muito alto! Tente novamente. ja foram {tentativas} tentativas.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero} em {tentativas} tentativas.")
            break
    else:
        print("Você perdeu!")
        break

