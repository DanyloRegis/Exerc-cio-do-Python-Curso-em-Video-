
def inverter_palavras():
    frase = input("Digite uma frase: ")
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    frase_invertida = ' '.join(palavras_invertidas)
    print("Frase com as palavras invertidas:", frase_invertida)