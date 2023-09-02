import pandas as pd
from drivers import WhatsApp
import time
import json

with open(comms, 'r') as json_file:
	com_data = json.load(json_file)


def main():
	pass




if __name__ == '__main__':
	print(com_data[0].keys())

	# parse_contacts(data, data_file)
	# automate_messages(data, cached_data)
