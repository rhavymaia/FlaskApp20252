from flask import Flask, request, jsonify

from models.Usuario import Usuario
from helpers.data import getInstituicoesEnsino

app = Flask(__name__)

usuario = Usuario(1, "João", "00011122233", "2025-10-09")
usuarios = [usuario]

# Instituições de Ensino.
instituicoesEnsino = getInstituicoesEnsino()


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
    instituicoesEnsinoJson = [instituicaoEnsino.to_json()
                              for instituicaoEnsino in instituicoesEnsino]
    return jsonify(instituicoesEnsinoJson), 200


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    ieDict = instituicoesEnsino[id].to_json()
    return jsonify(ieDict), 200


# todo: entregar endpoints completos de IE e Usuarios.
