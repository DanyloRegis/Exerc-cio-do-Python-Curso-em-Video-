lista_de_maiores = []
lista_de_menores = []
for i in range(3):
    nome = input("Digite seu nome: ")
    n = int(input("Digite seu ano de nasimento: "))
    ano = int(input("Digite o ano atual: "))
    idade = ano - n
    if idade >= 18:
        lista_de_maiores.append(nome)
    else:
        lista_de_menores.append(nome)
print(f"Lista de maiores de idade: {lista_de_maiores}")
print(f"Lista de menores de idade: {lista_de_menores}")