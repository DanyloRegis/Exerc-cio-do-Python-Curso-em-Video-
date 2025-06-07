def leiaint(msg):
    while True:
        n = input(msg)  # Usa a mensagem personalizada
        try:
            n = int(n)  # Tenta converter a entrada para um inteiro
            print("A variável é um inteiro.")
            return n  # Retorna o número inteiro
        except ValueError:
            print("Isso não é um número inteiro. Tente novamente.")

numero = leiaint("Digite um número inteiro: ")
print(f"O número digitado foi: {numero}")

