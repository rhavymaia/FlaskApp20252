from marshmallow import Schema, fields, validate


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


class UsuarioSchema(Schema):
    nome = fields.String(validate=validate.Length(min=2, max=255),
                         required=True, error_messages={"required": "O Nome do Usuário é obrigatório.", "length-min": "Tamanho inválido"})
    cpf = fields.String(validate=validate.Length(min=11, max=11),
                        required=True, error_messages={"required": "O CPF do Usuário é obrigatório.", "length": "Tamanho inválido"})
    nascimento = fields.Date(format="%Y-%m-%d", required=True,
                             error_messages={"required": "A Data de Nascimento do Usuário é obrigatória."})


if __name__ == "__main__":
    usuario = Usuario(1, "João", "00011122233", "2025-10-09")
    print(usuario)
