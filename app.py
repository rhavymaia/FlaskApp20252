import sqlite3

from helpers.application import app, api
from helpers.database import db, get_conn
from helpers.logging import logger

from resources.HomeResource import HomeResources
from resources.UsuariosResource import UsuariosResource, UsuarioResource

api.add_resource(HomeResources, '/')
api.add_resource(UsuariosResource, '/usuarios')
api.add_resource(UsuarioResource, '/usuarios/<string:id>')

# TODO: Implementar a migração para flask-restful


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

# TODO: Implementar a migração para flask-restful


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    return {}, 501


with app.app_context():
    db.create_all()
