import copy

from google.auth.transport import requests

from src.abstract_classes import API


class HeadHunterAPI(API):
    __HH_API_URL = 'https://api.hh.ru/vacancies'
    param_default = {
        'per_page': 50,
        'area': 1,
        'date': 7,
        'only_with_salary': True
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_default)

    def get_vacancies(self):
        response = requests.get(self.__HH_API_URL, params=self.param)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return None
