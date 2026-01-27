from flask import request
from flask_restful import Resource
from psycopg2 import Error
from marshmallow import ValidationError

from helpers.logging import logger
from helpers.database import get_conn
from models.Usuario import UsuarioSchema


class UsuariosResource(Resource):
    def get(self):
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

        except Error as e:
            logger.error(f"An SQL error occurred: {e}")
            return {"mensagem": "Problema na operação com os dados"}, 500

    def post(self):
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
            statement = "INSERT INTO tb_usuario (nome, cpf, nascimento) VALUES (%s, %s, %s) RETURNING id;"
            cursor.execute(statement, (nome, cpf, nascimento))

            # id = cursor.lastrowid
            row = cursor.fetchone()
            id = row[0]

            # Adicionar id do registro criado ao usuário de rotorno.
            usuarioJson.update({"id": id})

            return usuarioJson, 201

        except ValidationError as err:
            return err.messages, 400
        except Error as e:
            logger.error(f"An SQLite error occurred: {e}")
            return {"mensagem": "Problema na operação com os dados"}, 500
