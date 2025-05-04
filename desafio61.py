
p_um = int(input("Digite o um número: "))
n = int(input("Quantos termos você quer mostrar? "))
i = int(input("Digite a razão: "))

while n > 0:
    print(p_um, end=" ➤ ")
    p_um += i
    n -= 1
print("FIM")