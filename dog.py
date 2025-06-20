class Pet:
    def __init__(self, name: str, peso: float):
        self.name = name
        self.peso = peso
    
    
    def imprimir(self):
        print(f"Nome do pet: {self.name}, Peso: {self.peso} kg")
    def alimento(self,comida):
        self.peso + comida
        
class Abrigo:
    catalogo = []
    def adiconar(self, pet: Pet):
        self.catalogo.append(pet)
    def imprimir(self):
        print("Lista de Pets no Abrigo:")
        print("=================================")
        for pet in self.catalogo:
            pet.imprimir()
            print("---------------------------------")
        print("=================================")
        
# Exemplo de uso
abrigo = Abrigo()

while True:
    nome = input("Digite o nome do pet (ou 's' para encerrar ou l pra a lista dos pet): ")
    if nome.lower() == 'l':
        abrigo.imprimir()
        continue
    if nome.lower() == 's':
        print("Finalizado...")
        break
    peso = float(input("Digite o peso do pet: "))
    pet = Pet(nome, peso)
    abrigo.adiconar(pet)

