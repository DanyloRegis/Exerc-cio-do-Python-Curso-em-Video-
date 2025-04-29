
salario = float(input("Digite o salário do funcionário: "))

n = salario * 0.3

valor_da_casa = float(input("Digite o valor da casa: "))

tempo = int(input("Digite o tempo em anos para pagar a casa: "))

prestacao = valor_da_casa / (tempo * 12)

if prestacao > n:
    print("Empréstimo não concedido!")
elif prestacao <= n:
    print("Empréstimo concedido!")