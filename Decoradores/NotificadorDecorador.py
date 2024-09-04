from Notificador import Notificador

class NotificadorDecorador(Notificador):
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
        
    def enviar(self, msg: str):
        self.notificador.enviar(msg)