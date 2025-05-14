lista = ('bolo', 1.50, 'cafe', 2.50, 'sorvete', 3.50, 'pizza', 25.00, 'hamburguer', 15.00, 'batata frita', 10.00)

print("\nCatálogo de Produtos:")
print("=" * 30)
print(f"{'Produto':<20} {'Valor':>10}")
print("-" * 30)

# Percorre a lista em passos de 2
for i in range(0, len(lista), 2):
    produto = lista[i]
    valor = lista[i+1]
    print(f"{produto:<20} R$ {valor:>7.2f}")