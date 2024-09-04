import DecoradoresConcretos as dc
import NotificadoresEspecificos as ne


email = ne.NotificadorEmail()
sms = ne.NotificadorSMS()
wpp = ne.NotificadorWhatsApp()

email.enviar("Hola")
sms.enviar("como")
wpp.enviar("estas?")

email_firmado = dc.NotificadorConFirma(email, "Lucia Vazquez")
email_firmado.enviar("Funciona esto?")
email_encriptado_firmado = dc.NotificadorEncriptado(email_firmado)
email_encriptado_firmado.enviar("123")
email_aleatorio_encriptado_firmado = dc.NotificadorAleatorio(email_encriptado_firmado)
email_aleatorio_encriptado_firmado.enviar("A ver que sale")

sms_encriptado = dc.NotificadorEncriptado(sms)
sms_encriptado_firmado = dc.NotificadorConFirma(sms_encriptado, "Alumno")
sms_encriptado_firmado.enviar("Mensaje para SMS")


wpp_aleatorio = dc.NotificadorAleatorio(wpp)
wpp_aleatorio_encriptado = dc.NotificadorEncriptado(wpp_aleatorio)
wpp_aleatorio_encriptado_firmado = dc.NotificadorConFirma(wpp_aleatorio_encriptado, "Lucia")
wpp_aleatorio_encriptado_firmado.enviar("Mensaje para WhatsApp")