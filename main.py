import json
import random
from binance.client import Client

'''На случай если данные с фронтенда будут предоставляться в виде json файлов
напишем функцию для преобразования файлов в словари python'''


def load_json(file_name):
    with open(file_name, 'r') as f:
        dict_file = json.load(f)
    return dict_file


def create_orders(data):
    # Разбираем данные
    volume = data['volume']
    number = data['number']
    amountDif = data['amountDif']
    side = data['side']
    priceMin = data['priceMin']
    priceMax = data['priceMax']

    # Рассчитываем объем каждого ордера
    order_volume = volume / number

    # Создаем клиента Binance
    client = Client('API_KEY', 'API_SECRET')  # в этой строке нужно заменить API KEY и API SECRET

    # Создаем ордеры
    for i in range(number):
        # Выбираем случайный объем в пределах разброса
        order_volume_random = random.uniform(order_volume - amountDif, order_volume + amountDif)

        # Выбираем случайную цену в пределах диапазона
        order_price = random.uniform(priceMin, priceMax)

        # Создаем ордер
        order = client.create_order(
            symbol='BNBUSDT',
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=order_volume_random,
            price=order_price
        )

        print(f'Создан ордер: {order}')


data1 = {
    "volume": 10000.0,  # Объем в долларах
    "number": 5,  # На сколько ордеров нужно разбить этот объем
    "amountDif": 50.0,
    # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
    "side": "SELL",  # Сторона торговли (SELL или BUY)
    "priceMin": 200.0,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
    "priceMax": 300.0  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
}
data2 = {
    "volume": 1000.0,  # Объем в долларах
    "number": 4,  # На сколько ордеров нужно разбить этот объем
    "amountDif": 40.0,
    # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
    "side": "BUY",  # Сторона торговли (SELL или BUY)
    "priceMin": 20.0,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
    "priceMax": 200.0  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
}
# Тестируем написанный код
print('тест 1')
try:
    orders = create_orders(data1)
    print('операция проведена успешно')
except:
    print('упс, что-то пошло не так')

print('Тест 2')
try:
    orders = create_orders(data2)
    print('Операция проведена успешно')
except:
    print('упс,что-то пошло не так')
print('тест3')
try:
    orders=create_orders(load_json('data.json'))
    print('Операция проведена успешно')
except:
    print('упс, что-то пошло не так')
