# cw_4_vacancies
## Курсовая работа №4: Vacancies

Программа получает информацию о вакансиях с разных платформ в России, сохраняет ее в файл и позволяет удобно работать с ней.

## Рееализации
Создаёт абстрактный класс для работы с API сайтов с вакансиями. Реализованы классы, наследующиеся от абстрактного класса, для работы с конкретными платформами. Классы умеют подключаться к API и получают вакансии.

## Платформы для сбора вакансий
 hh.ru (ссылка на API: https://github.com/hhru/api)
 superjob.ru (ссылка на API: https://api.superjob.ru/)

Прежде чем начать использовать API от SuperJob, необходимо зарегистрироваться (https://www.superjob.ru/auth/login/) и получить токен для работы. Подробная инструкция дается по ссылке описания документации в разделе Getting started: https://api.superjob.ru/#gettin. При регистрации приложения можно указать произвольные данные.
## Выходные данные
Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.
