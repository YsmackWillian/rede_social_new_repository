import sqlite3
from DataBase.UsuarioDAO import *
from DataBase.ComentarioDAO import *
def criarTabelas():
        conn = sqlite3.connect('redeSocial.db')
        cursor = conn.cursor()

        cursor.execute("""create table Usuario
                        (id integer primary key autoincrement,
                        nome varchar (100),
                        email varchar (100),
                        senha varchar (100),
                        dataNascimento date,
                        profissao varchar (50),
                        genero varchar (15),
                        cidade varchar (50),
                        estado varchar (50),
                        pais varchar (50))
                        """)

        cursor.execute("""create table comentario
                        (mensagem text,
                        dataHora datetime)
                        """)

def criarUsuario():
    nome = input("nome: ")
    email = input("email: ")
    senha = input("senha:")
    dataNascimento = input("formato (aaaa-mm-dd): ")
    profissao = input("profissão: ")
    genero = input("Gênero: ")
    cidade = input("cidade: ")
    estado = input("estado: ")
    pais = input("pais: ")

    usuario = Usuario(nome, email, senha, dataNascimento, profissao, genero, cidade, estado, pais)
    usuarioDAO = UsuarioDAO()

    usuarioDAO.insert(usuario)

def exibirMenu():
    print("""
            Menu\n
            1 - Criar Tabelas\n
            2 - Inserir Dados do Usuário\n
            3 - Atualizar Dados do Usuario\n
            4 - Deletar Usuario\n
            5 - Comentar\n
            0 - Sair\n""")

def main(args=[]):
    continuar = True

    while (continuar):

        exibirMenu()

        try:

            op_escolhida = int(input("Escolha uma das opções: "))
            if op_escolhida == 0:
                print("Saindo...")
                continuar = False
            elif op_escolhida == 1:
                criarTabelas()
            elif op_escolhida == 2:
                criarUsuario()
            elif op_escolhida == 3:
                usuarioDAO = UsuarioDAO()
                usuarioDAO.atualizar()
            elif op_escolhida == 4:
                usuarioDAO = UsuarioDAO()
                email = input("Email que deseja deletar! ")
                usuarioDAO.deletar(email)
            elif op_escolhida == 5:
                text = input("Informe o seu comentario:")
                comentario = Comentario(text)
                comentarioDAO = ComentarioDAO()
                comentarioDAO.inserirComentario(comentario)

        except ValueError:
            print("Erro")


if (__name__ == "__main__"):
    main()
