import sqlite3

def get_connection():
    conn = sqlite3.connect("cinema.db")
    return conn

def criar_tabelas():
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            duracao INTEGER NOT NULL
        )
    """)
    conn.comite()
    conn.close()