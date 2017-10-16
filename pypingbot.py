import os
import time
import smtplib
import requests

hostname = "google.com" 
notf_ping = False
notf_no_ping = False

def notificacion(mensaje):
	id = ''
	token = ''
	url = 'https://api.telegram.org/bot'+ token +'/sendMessage'
	params = {
		'chat_id': id,
		'text' : mensaje
	}
	try:
		resultado = requests.post(url, params=params)
		print('Notificacion enviada: ' + mensaje)
	except:
		print('Error al enviar notificacion ' + mensaje )


while (True):
	print (time.strftime("%d/%m/%Y %H:%M:%S"))
	response = os.system("ping -n 1 " + hostname)	
	
	if response == 0:
		print (hostname, 'is up!')
		if notf_ping == True:	
			print()
		else:
			notificacion('La ip: ' + hostname + ' esta up!!' )
			notf_ping = True
			notf_no_ping = False
	else:
		print (hostname, 'is down!')
		if notf_no_ping == True:
			print()
		else:
			notificacion('La ip: ' + hostname + ' esta down!!' )
			notf_no_ping = True
			notf_ping = False	

	time.sleep(300)


