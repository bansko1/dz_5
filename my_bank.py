"""
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
def my_bank():
    count = 0
    purchases = []
    goods = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if str(choice) == '1':
            sum = input('Введите сумму на сколько пополнить счет: ')
            count = count + int(sum)
        elif str(choice) == '2':
            purchase = input('Введите сумму покупки: ')
            if int(purchase) <= count:
                good = input('Введите название покупки: ')
                count = count - int(purchase)
                purchases.append(purchase)
                goods.append(good)
            else:
                print('Денег не хватает, пополните счет')
        elif choice == '3':
            print('История покупок:')
            for i in range(len(goods)):
                hist = f'товар: {goods[i]}, стоимость: {purchases[i]}'
                print(i + 1, hist)
        elif choice == '4':
            print('Остаток днег на счете:', count)
            break
        else:
            print('Неверный пункт меню')
if __name__ == '__main__':
    my_bank()