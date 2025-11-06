import sqlite3
from flask import Flask, request, jsonify

from models.Usuario import Usuario
from helpers.data import getInstituicoesEnsino

app = Flask(__name__)

usuario = Usuario(1, "João", "00011122233", "2025-10-09")
usuarios = [usuario]

# Instituições de Ensino.
instituicoesEnsino = getInstituicoesEnsino()

DATABASE_NAME = "censoescolar.db"


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
def setUsuarios():
    data = request.get_json()

    usuario = {"nome": data['nome']}
    usuarios.append(usuario)

    return usuario, 201


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


# todo: entregar endpoints completos de IE e Usuarios.
