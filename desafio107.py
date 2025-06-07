from uteis import desporcenoto, metade, dobro
n= float(input('Digite um valor: R$ '))
print(f'Aumentando 10% temos R${desporcenoto(n):.2f}')
print(f'A metade de R${n} é R$ {metade(n):.2f}')
print(f'O dobro de R${n} é R$ {dobro(n):.2f}')