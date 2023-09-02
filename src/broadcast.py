from drivers import WhatsApp
from parser import parse_data



def automate_messages():
	messenger = WhatsApp()

	for user in data:
		messenger.find_user(str(user['Cell']))
		messenger.send_picture("../assets/anuncio.jpeg", 'Aproveite as ferias!!!!')
		messenger.send_message(user['msg'])
		cached_data[user['Nome']] = user['Cell']
		time.sleep(10)