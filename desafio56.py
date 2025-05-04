menor = 0
maior = 0
menor_nome = ''
maior_nome = ''
media = 0

for i in range(3):
    print(f"----- {i+1}º Pessoa -----")
    name = input("Digite seu nome: ")
    n = int(input("Digite sua idade: "))
    media += n
    
    if i == 0:
        maior = n
        menor = n
        menor_nome = name
        maior_nome = name
    else:
        if n > maior:
            maior = n
            maior_nome = name
        if n < menor:
            menor = n
            menor_nome = name

print(f"O mais velho é {maior_nome} com {maior} anos e o mais novo é {menor_nome} com {menor} anos. A média de idade foi de {media/3:.1f} anos.")