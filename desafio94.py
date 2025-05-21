lista = []
pessoa = {}
res = 'S'  # Inicializa res para entrar no loop

print('-=' * 30)
print('CADASTRO DE PESSOAS'.center(60))
print('-=' * 30)

while True:
    if res in 'Ss':
        pessoa.clear()  # Limpa o dicionário para novo cadastro
        
        # Validação do nome
        while True:
            nome = input('Nome: ').strip()
            if nome.replace(' ', '').isalpha():
                pessoa['nome'] = nome
                break
            print('\033[1;31mERRO! Digite um nome válido (apenas letras).\033[m')

        # Validação do sexo
        while True:
            pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
            if pessoa['sexo'] in 'MF':
                break
            print('\033[1;31mERRO! Digite apenas M ou F.\033[m')

        # Validação da idade
        while True:
            try:
                pessoa['idade'] = int(input('Idade: '))
                if pessoa['idade'] > 0:
                    break
                print('\033[1;31mERRO! Idade deve ser maior que 0.\033[m')
            except ValueError:
                print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

        lista.append(pessoa.copy())

        # Validação para continuar
        while True:
            res = input('Quer continuar? [S/N] ').upper()[0]
            if res in 'SN':
                break
            print('\033[1;31mERRO! Responda apenas S ou N.\033[m')

    elif res in 'Nn':
        break

# Análise dos dados
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')

if len(lista) > 0:
    media = sum(p['idade'] for p in lista) / len(lista)
    print(f'Média de idade: {media:.1f} anos')

    mulheres = [p['nome'] for p in lista if p['sexo'] == 'F']
    print('Mulheres cadastradas:', ', '.join(mulheres) if mulheres else 'Nenhuma mulher cadastrada')

    print('Pessoas com idade acima da média:')
    for p in lista:
        if p['idade'] > media:
            print(f"   - Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}")

print('-=' * 30)
print('\033[1;32mPrograma encerrado com sucesso!\033[m')