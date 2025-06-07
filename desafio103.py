def ficha(nome='<Jogador_Desconhecido>', jogos=0):
    dados = {
        "Nome": nome,  # Valor associado à chave "Nome"
        "Jogos": jogos,
        "gols": [],
    }
    
    for i in range(jogos):
        # Coletando o número de gols para cada jogo e adicionando à lista
        gols = int(input(f"Digite o número de gols que ele fez no jogo {i + 1}: "))
        dados["gols"].append(gols)  # Adiciona o número de gols à lista

    # Exibindo os dados coletados
    print(f"{dados['Nome']} - Número de jogos: {dados['Jogos']} - Total de gols: {sum(dados['gols'])}")

# Chamando a função com um exemplo
ficha()
