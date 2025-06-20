class Tv:
    def __init__(self):
        self.ligado = False
        self.maior_canal = 100
        self.menor_canal = 1
        self.menor_volume = 0
        self.maior_volume = 99
        self.canal = 1
        self.volume = 0
        #---------------------------------------
    def ligar(self):
        self.ligado = True 
        #---------------------------------------
    def desligar(self):
        self.ligado = False
    #---------------------------------------
    def subir_canal(self):
        if not self.ligado:
            return
        if self.canal < self.maior_canal:
            self.canal += 1
    #---------------------------------------
    def descer_canal(self):
        if not self.ligado:
            return
        if self.canal > self.menor_canal:
            self.canal -= 1
    #---------------------------------------
    def subir_volume(self):
        if not self.ligado:
            return
        if self.volume < self.maior_volume:
            self.volume += 1
    #---------------------------------------
    def descer_volume(self):
        if not self.ligado:
            return
        if self.volume > self.menor_volume:
            self.volume -= 1
    #---------------------------------------
    def __str__(self) -> str:
        return f'TV {"ligada" if self.ligado else "desligada"}, Canal: {self.canal}, Volume: {self.volume}'
        

minha_tv = Tv()
minha_tv.subir_canal()  # Sobe o canal
# Exemplo de uso
print(minha_tv)  # TV desligada, Canal: 1, Volume: 0