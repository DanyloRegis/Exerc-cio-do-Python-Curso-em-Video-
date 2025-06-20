class Bixo:
    def __init__(self, name):
        self.name = name
    
    def fazer_som(self):
        pass
    
class Gato(Bixo):
    def fazer_som(self):
        return "Miau"

class Vaca(Bixo):
    def fazer_som(self):
        return "Mugido"
    

class Pinto(Bixo):
    def fazer_som(self):
        return "Pio"    
    
##############################

gato = Gato("Neko")
vaca = Vaca("Mimosa")
pinto = Pinto("Pintinho")

print(f"O gato {gato.name} faz: {gato.fazer_som()}")
print(f"A vaca {vaca.name} faz: {vaca.fazer_som()}")
print(f"O pinto {pinto.name} faz: {pinto.fazer_som()}")
