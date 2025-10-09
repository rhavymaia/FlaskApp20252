class Usuario():
    def __init__(self, id, nome, cpf, nascimento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

    def __repr__(self):
        return f'<Usuario {self.nome}, {self.cpf}, {self.nascimento}>'

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "nascimento": self.nascimento}


print(__name__)
if __name__ == "__main__":
    usuario = Usuario(1, "João", "00011122233", "2025-10-09")
    print(usuario)
