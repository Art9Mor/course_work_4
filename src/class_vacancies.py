class Vacancies:
    """
    Class for working with vacancies
    """

    all_vacancies = []
    request_string = ''

    def __init__(self, vacancy_data) -> None:
        self.name = vacancy_data['name']
        self.requirement = vacancy_data['requirement']
        self.responsibility = vacancy_data['responsibility']
        self.salary = vacancy_data['salary']
        self.salary_currency = vacancy_data['salary_currency']
        self.url = vacancy_data['url']
        self.employer = vacancy_data['employer']

    def get_info(self) -> None:
        print('-' * 50)
        print(f'Employer: {self.employer[:100]}')
        print(f'Profession: {self.name}')
        if self.requirement is None:
            print('Requirements not specified.')
        else:
            print(f'Requirements: {self.requirement[:100]}...')
        if self.responsibility is None:
            print('Field of activity not specified.')
        else:
            print(f'Field of activity: {self.responsibility[:100]}...')
        print(f'Salary expectations: {self.salary} {self.salary_currency}.')
        print(f'Job vacancy link - {self.url}')
        print('-' * 50)
        print()

    def __len__(self) -> int:
        return len(Vacancies.all_vacancies)

    @classmethod
    def clear_vacancies_list(cls) -> None:
        cls.all_vacancies = []

    @classmethod
    def reformat_data(cls) -> list:
        reformat_data = []
        for vacancy in cls.all_vacancies:
            reformat_data.append(vacancy.__dict__)
        return reformat_data
