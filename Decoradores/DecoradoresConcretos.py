from NotificadorDecorador import NotificadorDecorador
import random

class NotificadorConFirma(NotificadorDecorador):
    def __init__(self, notificador, firma: str):
        super().__init__(notificador)
        self.sig = firma 

    def enviar(self, msg: str):
        super().enviar(msg +" " +self.sig)
        
class NotificadorEncriptado(NotificadorDecorador):
    def enviar(self, msg: str):
        enc = msg[::-1]
        super().enviar(enc)

class NotificadorAleatorio(NotificadorDecorador):
    def enviar(self, msg: str):
        msg_to_list = list(msg)
        random.shuffle(msg_to_list)
        mix = ''.join(msg_to_list)
        super().enviar(mix)
