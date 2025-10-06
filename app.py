from flask import Flask, request, jsonify
from models.InstituicaoEnsino import InstituicaoEnsino

app = Flask(__name__)

usuarios = [{'nome': 'João'}]

ie = InstituicaoEnsino("25000012", "EMEF JOAO ALVES",
                       25, "2501005", 779, 0, 104, 43)
instituicoesEnsino = [ie]


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
    return instituicoesEnsino, 200


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    ieDict = instituicoesEnsino[id].to_json()
    return jsonify(ieDict), 200
