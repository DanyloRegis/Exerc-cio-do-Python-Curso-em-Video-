
nome = str(input("Digite o nome do aluno: "))
santo = "Santo"

if santo in nome or santo.lower() in nome:
    print(f"O nome contém a palavra '{santo}'.")
else:
    print(f"O nome não contém a palavra '{santo}'.")