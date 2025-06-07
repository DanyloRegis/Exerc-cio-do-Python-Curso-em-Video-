from uteis import desporcenoto, metade, dobro, moeda

n = float(input('Digite um valor: R$ '))

# Use the moeda function to format the output
print(f'Aumentando 10% temos {moeda(desporcenoto(n))}')
print(f'A metade de {moeda(n)} é {moeda(metade(n))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
