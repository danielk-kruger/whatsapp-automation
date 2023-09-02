import json
import pandas as pd
import os, os.path

class Parser
	file_paths = []
	dir_path = "data"

	def __init__(self):
		self.init_datasets()


	# Here we get all our datasets and store into an array of dictionaries
	# This way we can distinguish what is a file and what isn`t.
	
	# base data structure.
	# file_paths -> [
	# 	'comms.json',
	# 	'settings.json',
	# 	{ 'contacts': { 'test_contacts.csv': 'data/contacts/test_contacts.csv' }}
	#	... etc
	# ]
	def init_datasets(self):
		for entry in os.listdir(dir_path):				
			if os.path.isdir(entry):
				entries = [self.filter_entries(entry)]
				self.set_filepath({ 
					self.get_name(entry): [{ 
						self.get_name(deep_entry): deep_entry 
					} for deep_entry in entries]
				})
			
			self.set_filepath(os.path.join(dir_path, entry))

	def set_filepath(self, file):
		print(f"Found file: {self.get_name(file)}")
		self.file_paths.append(file)

	def filter_entries(self, entry):
		return [os.path.join(self.dir_path, file) for file in entry if self.is_dataset(file)]

	def get_filepaths(self):
		return self.file_paths

	def get_name(self, file_path):
		return os.path.basename(file_path)

	def is_dataset(self, data_file):
		return entry.endswith('.csv') or entry.endswith('.json')


class Contacts(Parser):
	# list = []

	def __init__(self, contact, list=[]):
		# self.list = []
		self.list = self.get_contactlists()
		self.contact = contact if contact is not '' else self.list[0]


	def get_contactlists(self):
		for item in self.get_filepaths():
			contacts = item['contacts'].keys()
			print(contacts)

	# Return the file name if it is inside 
	def contact_selecto(self, file_name):
		names = [self.get_name(file) for file in self.list]
		if file_name in names:
			return file_name

	def parse_contacts(self):
		df = pd.read_csv(file, delimiter=";", encoding='latin1')
		data = []

		for i in df.index:
			data.append({
				'Nome': df['Nome'][i],
				'Sexo': df['Sexo'][i],
				'Cell': df['Telefone'][i],
			})

		return data

	def set_list(self, new_list):
		self.list = new_list

class Comms(Parser):
	options = []

	def get_comms(self):
		options = []
		comms = ""

		try:
			with open(comms_file, 'r') as json_file:
				comms = json.load(json_file)

			for com_option in comms[0]:
				options.append(com_option)
			
		except FileNotFoundError:
			print("File not found")

	def get_comm(key):
		for option in self.options:
			if (option.keys()[key] == key):
				return option.values()