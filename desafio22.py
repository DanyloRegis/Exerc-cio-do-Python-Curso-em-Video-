nome = str(input("Digite o nome do aluno: ")).strip()

# Convertendo para maiúsculas
texto_maiusculo = nome.upper()
print(f"O nome em maiúsculas é: {texto_maiusculo}")

# Convertendo para minúsculas
texto_minusculo = nome.lower()
print(f"O nome em minúsculas é: {texto_minusculo}")

# Contando o número de letras (sem espaços)
letras_sem_espacos = len(nome.replace(" ", ""))
print(f"Número de letras (sem espaços): {letras_sem_espacos}")

# Pegando o primeiro nome (split divide a string em partes separadas por espaço)
primeiro_nome = nome.split()[0]  # Pega a primeira palavra
numero_letras_primeiro_nome = len(primeiro_nome)

print(f"O primeiro nome é '{primeiro_nome}' e tem {numero_letras_primeiro_nome} letras.")