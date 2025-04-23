import random
# Atividade 02 - Gerar um número aleatório entre 1 e 10
def main():
    n1 = random.randint(1, 10)
    return n1

print("Deseja gerar um número aleatório entre 1 e 10? (Y/n)")
resposta = input()
if resposta.lower() == 'y' or resposta.lower() == 'Y':
    numero = main()
    print("O número gerado é:", numero)
else:
    print("Você escolheu não gerar um número aleatório.")
