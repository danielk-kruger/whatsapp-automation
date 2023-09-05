import os
import os.path

import pandas as pd
from utils import flatten


class Parser:
    file_paths = {}
    selected_file = ''

    def __init__(self, dir_path=(os.path.join(os.getcwd(), 'src/data'))):
        self.dir_path = dir_path
        print(self.dir_path)
        self.init_datasets()

    def init_datasets(self):
        for entry in os.listdir(self.dir_path):
            entry_path = os.path.join(self.dir_path, entry)

            if os.path.isdir(entry_path):
                self.file_paths[self.get_name(entry)] = flatten([{
                    self.get_name(deep_entry).split('.csv')[0]:
                        os.path.join(entry_path, deep_entry)
                } for deep_entry in os.listdir(entry_path)])

            # case its a basic file
            self.set_filepath(entry_path)

    @staticmethod
    def parse_contacts(self, file=None):
        if not file or os.path.exists(file):
            file = self.get_selected_file()

        df = pd.read_csv(file, delimiter=";", encoding='latin1')
        data = []

        for i in df.index:
            data.append({
                'Nome': df['Nome'][i],
                'Sexo': df['Sexo'][i],
                'Cell': df['Telefone'][i],
            })

        return data

    def set_filepath(self, file):
        if os.path.isdir(file):
            print(f"Found directory: {self.get_name(file)}")
            return
        else:
            print(f"Found file: {self.get_name(file)}")

        self.file_paths[self.get_name(file).split('.json')[0]] = file

    def filter_entries(self, entry):
        return [file for file in os.listdir(entry) if self.is_dataset(file)]

    def get_filepaths(self):
        return self.file_paths

    def get_contactlist(self):
        user_list = self.get_filepaths().get('contacts')
        print([key for key in user_list.keys()])

    def select_contact(self, key):
        file = self.file_paths.get('contacts').get(key)
        print(file)
        self.set_selected_file(file)

    @staticmethod
    def get_name(file_path):
        return os.path.basename(file_path)

    @staticmethod
    def is_dataset(data_file):
        return data_file.endswith('.csv') or data_file.endswith('.json')

    def set_selected_file(self, path):
        self.selected_file = path

    def get_selected_file(self):
        return self.selected_file

# class Comms(Parser):
#     options = []
#
#     def get_comms(self):
#         options = []
#         comms = ""
#
#         try:
#             with open(comms_file, 'r') as json_file:
#                 comms = json.load(json_file)
#
#             for com_option in comms[0]:
#                 options.append(com_option)
#
#         except FileNotFoundError:
#             print("File not found")
#
#     def get_comm(key):
#         for option in self.options:
#             if (option.keys()[key] == key):
#                 return option.values()
