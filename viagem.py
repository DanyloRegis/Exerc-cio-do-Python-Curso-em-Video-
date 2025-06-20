class Viagem:
    def __init__(self):
        self.cliente = ""
        self.destino = []
        self.local_escolhido = ""
    
    def adicionar_destino(self,destino):
        self.destino.append(destino)
        print(f"\nDestino {destino} adicionado com sucesso!")
    
    
    def escolher_destino(self):
        print("\nDestinos disponíveis:")
        for i in self.destino:
            print(f"- {i}")
        self.local_escolhido = input("Escolha o destino: ")
        if self.local_escolhido in self.destino:
            print(f"\nDestino escolhido: {self.local_escolhido}")
            print(f"\nViagem para {self.local_escolhido} agendada com sucesso para {self.cliente}!")
        else:
            print("\nDestino inválido. Por favor, escolha um destino válido.")
            self.escolher_destino()
            
    def nome_cliente(self):
        self.cliente = input("Digite o nome do cliente: ")
        self.escolher_destino()  # Fixed this line to actually call the method

passira = Viagem()
passira.adicionar_destino("Paris")
passira.adicionar_destino("Londres")    
passira.nome_cliente()