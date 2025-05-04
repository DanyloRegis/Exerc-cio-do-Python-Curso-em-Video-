n = int(input("Digite um número: "))
cont = 0
# Desafio 52
for i in range(1, n + 1):
    if n % i == 0:
        cont += 1
        print(f"\033[34m{i}", end="\033[30m ➤ ")  # Corrigido: vírgula antes de end
    else:
        print(f"\033[31m{i}", end="\033[30m ➤ ")  # Corrigido: vírgula antes de end
print("\033[35m Fim")  # Reseta a cor para o padrão após a impressão dos números
# Reseta a cor para o padrão após a impressão dos números

if cont == 2:
    print(f"\033[34m O número {n} é primo.")
else:
    print(f"\033[31m O número {n} não é primo.")
