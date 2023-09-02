import json
import pandas as pd
import os, os.path

class Parser
	file_paths = []

	def __init__(self):
		self.init_datasets()


	def init_datasets(self):
		dir_path = "data"
		for entry in os.listdir(dir_path):				
			if os.path.isdir(entry):
				self.set_filepath({ 
					os.path.basename(entry): [file for file in entry if self.is_dataset(file)]
				})
			
			self.set_filepath(os.path.join(dir_path, entry))

	def set_filepath(self, file):
		print(f"Found file: {os.basename(file)}")
		self.file_paths.append(file)

	def get_filepaths(self):
		return self.file_paths

	def is_dataset(self, data_file):
		return entry.endswith('.csv') or entry.endswith('.json')


class Contacts(Parser):
	list = []

	def __init__(self):
		self.get_contactlists()

	def get_contactlists(self):
		for item in self.get_filepaths():
			if os.path.isdir(item) and item == 'contacts':
				self.list = os.listdir(item)

	def parse_data(self):
		df = pd.read_csv(file, delimiter=";", encoding='latin1')
		data = []

		for i in df.index:
			data.append({
				'Nome': df['Nome'][i],
				'Sexo': df['Sexo'][i],
				'Cell': df['Telefone'][i],
			})

		return data

class Comms(Parser):
	options = []
	comms_file = "data/comms.json"

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