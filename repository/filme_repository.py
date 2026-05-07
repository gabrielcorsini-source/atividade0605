from db.database import get_connection
from model.filme import Filme
class FilmeRepository:

    def salvar(self, filme: Filme):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO filme (titulo, genero, duracao) VALUES (?, ?, ?)",
            ()
        )
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT titulo, genero, duracao FROM filme")
        rows = cursor.fetchall()
        conn.close()
        return [Filme(r[1], r[2], r[0]) for r in rows]