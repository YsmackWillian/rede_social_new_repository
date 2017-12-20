import sqlite3

from Model.Usuario import Usuario

class UsuarioDAO():

    def insert(self, usuario: Usuario):
        conn = sqlite3.connect('redeSocial.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO usuario(nome, email, senha, dataNascimento, profissao, genero, cidade, estado, pais)
                        VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (usuario.nome, usuario.email, usuario.senha, usuario.dataNascimento, usuario.profissao, usuario.genero, usuario.cidade, usuario.estado, usuario.pais))

        conn.commit()
        cursor.close()

    def atualizar(self):

        conn = sqlite3.connect('redeSocial.db')
        cursor = conn.cursor()

        novoNome = input("novo nome:")
        novaProfissao = input("nova profissao")

        cursor.execute("""UPDATE Usuario
                        SET nome = ?,
                        profissao = ?""", (novoNome, novaProfissao))

    def deletar(self, email):

        conn = sqlite3.connect('redeSocial.db')
        cursor = conn.cursor()

        cursor.execute("""DELETE from Usuario
                       where email = ?""", (email,))
