import sqlite3

DATABASE_NAME = "censoescolar.db"


def create_tables():
    print("Iniciando criação")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    with open('schema.sql') as f:
        print("Criando as tabelas")
        conn.executescript(f.read())

    print("Inserindo usuário padrão")
    cursor.execute("INSERT INTO tb_usuario (nome, cpf, nascimento) VALUES (?, ?, ?)",
                   ('João da Silva', '00011122255', '2025-10-30'))
    conn.commit()

    print("Fechar conexão")
    conn.close()


if __name__ == "__main__":
    create_tables()
