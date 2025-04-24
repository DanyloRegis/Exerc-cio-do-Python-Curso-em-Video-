
nome = str(input("Digite o nome do aluno: ")).strip()

primeiro_nome = nome.split()[0]  # Pega a primeira palavra
ultimo_nome = nome.split()[-1]  # Pega a última palavra

print(f"O primeiro nome é '{primeiro_nome}' e o último nome é '{ultimo_nome}'.")