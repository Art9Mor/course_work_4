import json

from src.abstract_classes import Saver


class InfoSaver(Saver):
    """
    Class for saving information to json file
    """
    def __init__(self, path='data/vacancies_data.json'):
        self.path = path

    def file_saving(self, data: list):
        """
        Saving data to a file
        :param data: list
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
