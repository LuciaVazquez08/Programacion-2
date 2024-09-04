from Notificador import Notificador

class NotificadorEmail(Notificador):
    def enviar(self, msg: str):
        print(f"Se envio el mail con el mensaje '{msg}'")

class NotificadorSMS(Notificador):
    def enviar(self, msg: str):
        print(f"Se envio en texto con el mensaje '{msg}'")

class NotificadorWhatsApp(Notificador):
    def enviar(self, msg:str):
        print(f"Se envio el wpp con el mensaje '{msg}'")

