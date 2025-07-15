import json

class Banco:
    def __init__(self,arquivo="dados_banco.txt"):
        self.contas = {}
        self.arquivo = arquivo
        self.carregar_dados()
    #---------------------------------------------------------------------------------------------------
    def adicionar_conta(self, conta):
        self.contas[conta.numero] = {
            "conta": conta.conta,
            "titular": conta.titular,
            "limite": conta.limite,
            "saldo": conta.saldo
        }
        self.salvar_dados()
    #---------------------------------------------------------------------------------------------------
    def salvar_dados(self):
        # Método para salvar os dados das contas em um arquivo
        with open(self.arquivo, 'w') as f:
            json.dump(self.contas, f, indent=4)
    #---------------------------------------------------------------------------------------------------
    def carregar_dados(self):
        # Método para carregar os dados das contas de um arquivo
        try:
            with open(self.arquivo, 'r') as f:
                self.contas = json.load(f)
        except FileNotFoundError:
            self.contas = {}
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de dados. O arquivo pode estar corrompido.")
            self.contas = {}
    #---------------------------------------------------------------------------------------------------
    def listar_contas(self):
        # Método para mostrar todas as contas cadastradas
        for numero, dados in self.contas.items():
            print(f"Número: {numero}")
            print(f"Conta: {dados['conta']}")
            print(f"Titular: {dados['titular']}")
            print(f"Saldo: R${dados['saldo']:.2f}")
            print(f"Limite: R${dados['limite']:.2f}")
            print("-------------------")
#=======================================================================================================
class ContaBancaria:
    def __init__(self, conta, numero, titular, limite, saldo=0.0):
        self.conta = conta
        self.numero = numero
        self.titular = titular
        self.limite = limite
        self.saldo = saldo
        
        
conta_maria = ContaBancaria(
    conta="Conta Corrente",
    numero="65432-1",
    titular="Maria Oliveira",
    limite=500.00
)

conta_joao = ContaBancaria(
    conta="Conta Poupança",
    numero="12345-6",
    titular="João Silva",
    limite=1000.00
)  
banco = Banco()
banco.adicionar_conta(conta_maria)
banco.adicionar_conta(conta_joao)
banco.listar_contas()
banco.apagar_conta(65432-1)
banco.listar_contas()