import sqlite3
from flask import Flask, request, jsonify
from marshmallow import ValidationError
from datetime import datetime

from models.Usuario import Usuario, UsuarioSchema
from helpers.data import getInstituicoesEnsino


app = Flask(__name__)

usuario = Usuario(1, "João", "00011122233", "2025-10-09")
usuarios = [usuario]

# Instituições de Ensino.
instituicoesEnsino = getInstituicoesEnsino()

DATABASE_NAME = "censoescolar.db"


def is_data_valida(data_string):
    try:
        datetime.strptime(data_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


@app.get("/usuarios")
def getUsuarios():
    return jsonify(usuarios)


@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    return jsonify(usuarios[id])


@app.post("/usuarios")
def setUsuario():

    try:
        usuarioJson = request.get_json()

        usuarioSchema = UsuarioSchema()

        usuarioData = usuarioSchema.load(usuarioJson)

        # Manipulação com o banco de dados.
        # conectar com o banco.
        conn = sqlite3.connect(DATABASE_NAME)

        # capturar o cursor
        cursor = conn.cursor()

        nome = usuarioData['nome']
        cpf = usuarioData['cpf']
        nascimento = usuarioData['nascimento']

        # consultar: execução da dml.
        statement = "INSERT INTO tb_instituicao(nome, cpf, nascimento) values(?, ?, ?)"
        cursor.execute(statement, (nome, cpf, nascimento))

        id = cursor.lastrowid

        # Commit - Confirma transação.
        cursor.commit()

        # Adicionar id do registro criado ao usuário de rotorno.
        usuarioJson.update({"id": id})

        return usuario, 201

    except ValidationError as err:
        return err.messages, 400


@app.get("/instituicoesensino")
def getInstituicoesEnsino():
    # conectar com o banco.
    conn = sqlite3.connect(DATABASE_NAME)

    # capturar o cursor
    cursor = conn.cursor()

    # consultar: execução da dml.
    statement = "SELECT * FROM tb_instituicao"
    cursor.execute(statement)

    # fetch
    resultset = cursor.fetchall()

    instituicaoEnsinoResponse = []
    for row in resultset:
        id = row[0]
        codigo = row[1]
        nome = row[2]
        instituicaoEnsino = {"id": id, "codigo": codigo, "nome": nome}
        instituicaoEnsinoResponse.append(instituicaoEnsino)

    # fechar a conexão
    conn.close()

    return instituicaoEnsinoResponse, 200


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    ieDict = instituicoesEnsino[id].to_json()
    return jsonify(ieDict), 200
