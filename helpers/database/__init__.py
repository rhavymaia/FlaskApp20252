import psycopg2
from flask import g

from helpers.application import app

DATABASE = "censoescolar.db"


def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = psycopg2.connect(
            dbname="censoescolar",
            user="pweb2",
            password="123456",
            host="localhost",
            port="5434"
        )

        # conn.row_factory = make_dicts
    return conn


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()
