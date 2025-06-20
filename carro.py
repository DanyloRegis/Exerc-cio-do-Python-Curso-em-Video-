class Carro:
    def __init__(self,modelo,cor):
        self.ligado = False
        self.velocidade = 0
        self.cor    = cor
        self.modelo = modelo
        self.acelerar = 10
        self.desacelerar = -10
        self.limite = 120
        self.minimo = 0
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} foi ligado.")
        else:
            print(f"O carro {self.modelo} já está ligado.")
    def desligar(self):
        if not self.ligado:
            print(f"O carro {self.modelo} já está desligado.")
        else:
            self.ligado = False
            print(f"O carro {self.modelo} está desligado.")
    def acelerarCaro(self):
        if self.ligado ==True:
            if self.velocidade == self.limite:
                print(f"O carro {self.modelo} não pode acelerar além de {self.limite} km/h.")
            else:
                self.velocidade = self.velocidade + self.acelerar
                print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")
    def desacelerarCarro(self):
        if self.ligado == True:
            if self.velocidade == self.minimo:
                print(f"O carro {self.modelo} já está parado.")
            else:
                self.velocidade = self.velocidade + self.desacelerar
                print(f"O carro {self.modelo} desacelerou para {self.velocidade} km/h.")
            
    def pararCarro(self):
        while self.velocidade > 0:
            self.desacelerarCarro()
        self.desligar()
    def corCarro(self):
        print(f"O modelo do carro e {self.modelo} a cor e {self.cor}.")
            

carro1 = Carro("Fusca", "azul")
carro1.corCarro()
carro1.ligar()
carro1.acelerarCaro()
carro1.acelerarCaro()
carro1.pararCarro()