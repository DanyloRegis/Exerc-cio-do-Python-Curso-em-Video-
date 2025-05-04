
p_um = int(input("Digite o um número: "))
n = int(input("Quantos termos você quer mostrar? "))
i = int(input("Digite a razão: "))
if n == 0 or i == 0:
    print("Você não quer mostrar nenhum termo.")
    exit()
elif n < 0:
    print("Número inválido! Tente novamente.")
    exit()
else:
    while n > 0:
        print(p_um, end=" ➤ ")
        p_um += i
        n -= 1
print("FIM")