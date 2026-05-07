import sqlite3

class FilmeRepository:
    def __init__(self):
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()

        # Cria a tabela caso não exista
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            duracao INTEGER NOT NULL
        )
        """)

        self.conn.commit()

    def salvar(self, filme):
        self.cursor.execute(
            "INSERT INTO filme (titulo, genero, duracao) VALUES (?, ?, ?)",
            (filme.titulo, filme.genero, filme.duracao)
        )

        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM filme")
        return self.cursor.fetchall()