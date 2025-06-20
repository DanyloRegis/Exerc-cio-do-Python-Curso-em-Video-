class cidadoao:
    def __init__(self, nome):
        self.nome = nome
        print(f"Bem-vindo, {self.nome}!")
        
    def __del__(self):
        print(f"Despedindo-se de {self.nome}!")
        
        
pessoa = cidadoao("João")
pessoa2 = cidadoao("Maria")

del pessoa
# Acessando o atributo nome do objeto pessoa2
print(pessoa2.nome)