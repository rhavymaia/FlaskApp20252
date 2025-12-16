import sqlite3
from flask import request
from marshmallow import ValidationError

from models.Usuario import UsuarioSchema
from helpers.application import app
from helpers.database import get_conn
from helpers.logging import logger


@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


@app.get("/usuarios")
def getUsuarios():
    logger.info("get - /usuarios")
    try:
        # conectar com o banco.
        conn = get_conn()

        # capturar o cursor
        cursor = conn.cursor()

        # consultar: execução da dml.
        statement = "SELECT * FROM tb_usuario"
        cursor.execute(statement)

        # fetch
        resultset = cursor.fetchall()

        usuariosEnsinoResponse = []
        for row in resultset:
            id = row[0]
            codigo = row[1]
            nome = row[2]

            instituicaoEnsino = {"id": id, "codigo": codigo, "nome": nome}

            usuariosEnsinoResponse.append(instituicaoEnsino)

        return usuariosEnsinoResponse, 200

    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500


@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    return {}, 501


@app.post("/usuarios")
def setUsuario():

    logger.info("get - /usuarios")
    try:
        usuarioJson = request.get_json()

        usuarioSchema = UsuarioSchema()

        usuarioData = usuarioSchema.load(usuarioJson)

        # Manipulação com o banco de dados.
        # conectar com o banco.
        conn = get_conn()

        # capturar o cursor
        cursor = conn.cursor()

        nome = usuarioData['nome']
        cpf = usuarioData['cpf']
        nascimento = usuarioData['nascimento']
        logger.info(f"{nome} - {cpf} - {nascimento}")

        # consultar: execução da dml.
        statement = "INSERT INTO tb_instituicao(nome, cpf, nascimento) values(?, ?, ?)"

        cursor.execute(statement, (nome, cpf, nascimento))

        id = cursor.lastrowid

        # Commit - Confirma transação.
        cursor.commit()

        # Adicionar id do registro criado ao usuário de rotorno.
        usuarioJson.update({"id": id})

        return usuarioJson, 201

    except ValidationError as err:
        return err.messages, 400
    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500


@app.get("/instituicoesensino")
def getInstituicoesEnsino():

    logger.info("get - /instituicoesensino")
    try:
        # conectar com o banco.
        conn = get_conn()

        # capturar o cursor
        cursor = conn.cursor()

        # consultar: execução da dml.
        statement = "SELECT * FROM tb_instituicao"
        cursor.execute(statement)

        # fetch
        resultset = cursor.fetchall()

        instituicoesEnsinoResponse = []
        for row in resultset:
            id = row["id"]
            codigo = row["codigo"]
            nome = row["nome"]
            instituicaoEnsino = {"id": id, "codigo": codigo, "nome": nome}
            instituicoesEnsinoResponse.append(instituicaoEnsino)

        return instituicoesEnsinoResponse, 200

    except sqlite3.Error as e:
        logger.error(f"An SQLite error occurred: {e}")
        return {"mensagem": "Problema na operação com os dados"}, 500


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    return {}, 501
