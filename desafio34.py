

salario = float(input("Digite o salário do funcionário: "))


print(f"Salário: R$ {salario:.2f}")

if salario <= 1250: 
    print(f"Novo salário: R$ {salario * 0.1:.2f}")
else:   
    print(f"Novo salário: R$ {salario * 0.15:.2f}")