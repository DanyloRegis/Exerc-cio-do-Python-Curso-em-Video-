class Livro:
    def __init__(self, titulo, autor, ano_publicacao,numero_paginas,genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.genero = genero
    
    def get_livro(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_publicacao": self.ano_publicacao,
            "numero_paginas": self.numero_paginas,
            "genero": self.genero
        }

    def set_livro_titulo(self, titulo):
        self.titulo = titulo

livro1= Livro("Fenomenologia do Espírito", "Georg Wilhelm Friedrich Hegel", 1807, 500, "Filosofia")

print(livro1.get_livro())

livro1.set_livro_titulo("Fenomenologia do Espírito - Edição Especial")
print(livro1.get_livro())