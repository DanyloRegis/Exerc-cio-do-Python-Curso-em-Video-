def fatorial(x, show=False):
    """
    Desafio 102
    """
    fat = 1  # Inicializa a variável fat
    if x < 0:
        return "ERRO: Fatorial de número negativo não existe."
    for i in range(x, 0, -1):  # Loop de x até 1
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= i  # Calcula o fatorial
    if show:
        print(fat)  # Mostra o resultado se show=True
    # Retorna o valor do fatorial

# Testes
print(fatorial(10, show=True))   # Mostra o processo e o resultado
print(fatorial(5, show=False))  # Retorna apenas o resultado (120)
print(fatorial(-3))             # Retorna mensagem de erro