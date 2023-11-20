class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Admin", "admin", "admin")
usuario2 = Usuario("Jeferson Silva", "jefs", "chatsenha")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2}