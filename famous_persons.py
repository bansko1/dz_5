import random


def get_random_person():
    '''
    Получить случайного человека (Имя, дата рождения)
    '''
    FAMOUS_PEOPLE = {
        'А.С.Пушкин': '06.06.1799',
        'Н.В.Гоголь': '01.04.1809',
        'М.Ю.Лермонтов': '15.10.1814',
        'Ф.М.Достоевский': '11.11.1821',
        'С.А.Некрасов': '10.12.1821',
        'Л.Н.Толстой': '09.09.1828',
        'А.П.Чехов': '29.01.1860',
        'М.А.Булгаков': '15.05.1891',
        'С.А.Есенин': '03.10.1895',
        'М.А.Шолохов': '24.05.1905'
    }
    # Выбираем случайного человека
    name, data = random.choice(list(FAMOUS_PEOPLE.items()))
    return name, data


def get_person_and_question():
    '''
    Задать вопрос по случайному человеку
    :return:
    '''
    name, data = get_random_person()
    answer = input(f'Когда родился {name}? ')
    if answer == data:
        print('Верно')
    else:
        print('Неверно')

if __name__ == '__main__':
    print('Проверка функции get_random_person()', get_random_person())