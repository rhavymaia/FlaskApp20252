import psycopg2
from psycopg2 import OperationalError

DATABASE_NAME = "censoescolar.db"


def create_tables():
    try:
        print("Iniciando criação")

        conn = psycopg2.connect(
            dbname="censoescolar",
            user="pweb2",
            password="123456",
            host="localhost",
            port="5434"
        )

        cursor = conn.cursor()

        with open('schema.sql') as f:
            print("Criando as tabelas")
            cursor.execute(f.read())

        print("Inserindo usuário padrão")
        cursor.execute("INSERT INTO tb_usuario (nome, cpf, nascimento) VALUES (%s, %s, %s)",
                       ('João da Silva', '00011122255', '2025-10-30'))
        conn.commit()

    except OperationalError as e:
        # Handle the error, print details, or log the error
        print(f"The connection failed: {e}")
        # Optional: Get the PostgreSQL error code
        if hasattr(e, 'pgcode'):
            print(f"PostgreSQL Error Code: {e.pgcode}")

    except psycopg2.Error as e:
        # Catch any other general psycopg2 errors
        print(f"A general psycopg2 error occurred: {e}")

    finally:
        print("Fechar conexão")
        conn.close()


if __name__ == "__main__":
    create_tables()
