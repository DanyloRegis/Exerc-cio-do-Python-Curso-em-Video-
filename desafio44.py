# Desafio 44 - Sistema de Pagamento
valor_produto = float(input("Digite o valor do produto: "))
if valor_produto <= 0:
    raise ValueError("Valor inválido! O valor do produto deve ser maior que zero.")
fomra_de_pagamento = int(input("Escolha a forma de pagamento:\n"
                            "[1] À vista\n"
                            "[2] 2x sem juros\n"
                            "[3] 3x ou mais com juros\n"
                            "[4] À vista no cartão\n"
                            "Sua opção: "))

if fomra_de_pagamento == 1:
    desconto = valor_produto * 0.1
    valor_final = valor_produto - desconto
    print(f"Valor final com desconto: R$ {valor_final:.2f}")
elif fomra_de_pagamento == 2:
    valor_final = valor_produto
    print(f"Valor final: R$ {valor_final:.2f}")
elif fomra_de_pagamento == 3:
    parcelas = int(input("Digite o número de parcelas: "))
    juros = valor_produto * 0.2
    valor_final = valor_produto + juros
    valor_parcela = valor_final / parcelas
    print(f"Valor final com juros: R$ {valor_final:.2f}")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")
elif fomra_de_pagamento == 4:   
    desconto = valor_produto * 0.05
    valor_final = valor_produto - desconto
    print(f"Valor final com desconto: R$ {valor_final:.2f}")
else:
    raise ValueError("Opção inválida! Escolha entre 1 e 4.")