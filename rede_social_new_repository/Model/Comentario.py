import datetime

class Comentario():

    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.dataHora = datetime.datetime.now()
