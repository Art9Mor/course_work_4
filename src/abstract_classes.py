from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def get_vacancies(self):
        ...

    @abstractmethod
    def add_profession(self, value):
        ...

    @abstractmethod
    def formated_data(self, data):
        ...


class Saver(ABC):

    @abstractmethod
    def __init__(self, path):
        ...

    @abstractmethod
    def file_saving(self, data):
        ...
