import copy
import os

import requests

from src.abstract_classes import API
from src.class_vacancies import Vacancies


class SuperJobAPI(API):
    """
    Obtaining information from the API of the superjob.ru website
    """
    __SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    __SJ_API_KEY = os.getenv('SECRET_KEY')

    param_default = {
        'count': 50,
        'town': 'Новосибирск',
        'period': 7,
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_default)

    def get_vacancies(self):
        """
        Receiving information via API about vacancies
        """

        headers = {'X-Api-App-Id': self.__SJ_API_KEY}

        response = requests.get(self.__SJ_API_URL, headers=headers, params=self.param)
        if response.status_code == 200:
            return response.json()['objects']
        else:
            return None

    def add_profession(self, value: str) -> None:
        """
        Adding the 'keyword' parameter to param
        :param value: string
        """
        self.param['keyword'] = value
        Vacancies.request_text = value

    def formated_data(self, data: list) -> list:
        """
        Data formatting
        :param data: list
        :return: list
        """

        work_data = []
        for item in data:
            if item['payment_to'] == 0:
                salary = item['payment_from']
            else:
                salary = item['payment_to']
            requirement = item['candidat']
            requirement = requirement.replace('\n', ' ')
            work_dict = {'name': item['profession'],
                         'requirement': requirement,
                         'responsibility': item['catalogues'][0]['title'],
                         'salary': salary,
                         'salary_currency': 'руб',
                         'url': item['link'],
                         'employer': item['firm_name']
                         }
            work_data.append(work_dict)
        return work_data
