"""
Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно
быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения). Структуру нужно сформировать
программно, т.е. запрашивать все данные у пользователя
"""

goods, order = [], 1
title, price, amount = None, None, None
while True:
    if title is None:
        temp = input('Введите название товара: ')
        if not temp.isalnum():
            print('Строчка не может быть пустой')
            continue
        title = temp
    if price is None:
        temp = input('Введите стоимость товара: ')
        if not temp.isdigit():
            print('Число должно быть целым')
            continue
        price = int(temp)
    if amount is None:
        temp = input('Введите количество: ')
        if not temp.isdigit():
            print('Число должно быть целым')
            continue
        amount = int(temp)
    temp = input('Введите единицу измерения: ')
    if not temp.isalpha():
        print('Строчка не может быть пустой')
        continue
    unit = temp
    goods.append((order, {
        'название': title,
        'цена': price,
        'количество': amount,
        'ед': unit
    }))
    title, price, amount = None, None, None
    order += 1
    print('\n'.join(map(str, goods)))
    q = input('Для окончания формирования списка введите "д" (иначе Enter)')
    if q.lower() == 'д':
        break
analitics = {'название': [], 'цена': [], 'количество': [], 'ед': set()}
for _, item in goods:
    analitics['название'].append(item['название'])
    analitics['цена'].append(item['цена'])
    analitics['количество'].append(item['количество'])
    analitics['ед'].add(item['ед'])
print(analitics)
