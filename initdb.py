import sqlite3

DATABASE_NAME = "censoescolar.db"

tables = [
    """
        CREATE TABLE IF NOT EXISTS tb_instituicao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL,
                nome TEXT NOT NULL,
                co_uf INTEGER NOT NULL,
                co_municipio INTEGER NOT NULL,
                qt_mat_bas INTEGER NOT NULL,
                qt_mat_prof INTEGER NOT NULL,
                qt_mat_esp INTEGER NOT NULL
        )
    """,
    """
        CREATE TABLE IF NOT EXISTS tb_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                nascimento DATE NOT NULL
        )
    """
]


def create_tables():
    print("Iniciando criação")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    for table in tables:
        print("Criando as tabelas")
        cursor.execute(table)
    conn.commit()
    print("Fechar conexão")
    conn.close()


if __name__ == "__main__":
    create_tables()
