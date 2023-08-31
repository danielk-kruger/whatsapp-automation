import pandas as pd
from drivers import WhatsApp
import time

data_file = "data/test_contacts.csv"
cached_data = {}
data = []

def automate_messages(data, cache):
	messenger = WhatsApp()

	for user in data:
		messenger.find_user(str(user['Cell']))
		messenger.send_picture("../assets/anuncio.jpeg", 'Aproveite as ferias!!!!')
		messenger.send_message(user['msg'])
		cached_data[user['Nome']] = user['Cell']
		time.sleep(10)	

def parse_contacts(data, file):
	df = pd.read_csv(file, delimiter=";", encoding='latin1')

	for i in df.index:
		greeting = 'Ola '

		if df['Sexo'][i] == 'M':
			greeting += 'Sr. '
		else:
			greeting += 'Sra. '

		msg = greeting + df['Nome'][i] + '\n\nEsta é uma mensagem de texto automática enviada para vários contatos de uma só vez para fins de teste\n\n\n~Daniel'
		data.append({
			'Nome': df['Nome'][i],
			'Sexo': df['Sexo'][i],
			'Cell': df['Telefone'][i],
			'msg': msg
		})

if __name__ == '__main__':
	parse_contacts(data, data_file)
	automate_messages(data, cached_data)
