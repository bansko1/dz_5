'''

В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.

'''
import os
import shutil
import sys
from famous_persons import get_person_and_question
from my_bank import my_bank
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name = input('Введите название создаваемой папки: ')
        if not os.path.exists(name):
            os.mkdir(name)
    elif choice == '2':
        name = input('Введите название удаляемой файла/папки: ')
        if os.path.exists(name):
            os.rmdir(name)
    elif choice == '3':
        name = input('Введите название копируемой файла/папки: ')
        name_new = input('Введите новое название копируемой файла/папки: ')
        shutil.copy(name, name_new)
    elif choice == '4':
        # Список файлов и папок
        print(os.listdir())
    elif choice == '5':
        # Список только папок
        content = os.listdir()
        images = []
        for file in content:
            if not os.path.isfile(file):
                images.append(file)
        print(images)
    elif choice == '6':
        # Список только файлов
        content = os.listdir()
        images = []
        for file in content:
            if os.path.isfile(file):
                images.append(file)
        print(images)
    elif choice == '7':
        # Пути, где питон ищет файлы
        print(sys.path)
    elif choice == '8':
        print('Создатель программы - Стив Джобс')
    elif choice == '9':
        rounds = int(input('Сколько раз будем играть?'))

        for i in range(rounds):
            get_person_and_question()
        print('Пока!')
    elif choice == '10':
        my_bank()
    elif choice == '11':
        print('Текущая дериктория', os.getcwd())
        key = input('Введите 1, чтобы сменить текущую дерикторию')
        if key == '1':
            path = input('Введите путь к новой дериктории: ')
            os.chdir(path)
    elif choice == '12':
        print('*** Конец работы ***')

        break
    else:
        print('Неверный пункт меню')