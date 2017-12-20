import sqlite3
from Model.Comentario import Comentario

class ComentarioDAO():

    def inserirComentario(self, comentario):

        conn = sqlite3.connect('redeSocial.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO comentario(mensagem, dataHora)
                        VALUES(?, ?)""", (comentario.mensagem, comentario.dataHora))

        conn.commit()
        cursor.close()
