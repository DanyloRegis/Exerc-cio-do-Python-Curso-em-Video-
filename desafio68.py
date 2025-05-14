import random

numeros = [1, 2, 3, 4, 5]
n = 0
jogar = ''
vitoria = 0
perda = 0
while True:
    n = int(input("Digite um número inteiro positivo entre 1 e 5 : "))
    escolha = random.choice(numeros)
    if n <= 0:
        print(" fim de execução")
        continue
    elif n> 5:
        print("Número maior que 5, escolha outro número")
        continue
    else:
        print("Você quer ir de par ou impar? (P/I)")
        jogar = input("Digite P para par ou I para ímpar: ").upper()
            
        if jogar == "P":
            if n % 2 == 0:
                print("Você ganhou!")
                vitoria += 1
                continue
            else:
                print("Você perdeu!")
                perda += 1
                break
        elif jogar == "I":
            if n % 2 != 0:
                print("Você ganhou!")
                vitoria += 1
                continue
                    
            else:
                print("Você perdeu!")
                perda += 1
                break
        else:
                print("Opção inválida! Tente novamente.")
                continue
print(f"Você ganhou {vitoria} vezes e perdeu {perda} vezes.")
print("Fim de execução")

