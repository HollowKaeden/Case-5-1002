# Ваня Француз
import requests


def get_cities():
    r = requests.get('http://dt.miet.ru/ppo_it/api',
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    print(r.json()['data'])
    # Возвращает массив со словарями
    # [{'city_id': 1, 'city_name': 'Алмазный'},
    #  {'city_id': 2, 'city_name': 'Восточный'},
    #  {'city_id': 3, 'city_name': 'Западный'},
    #  {'city_id': 4, 'city_name': 'Заречный'},
    #  {'city_id': 5, 'city_name': 'Курортный'},
    #  {'city_id': 6, 'city_name': 'Лесной'},
    #  {'city_id': 7, 'city_name': 'Научный'},
    #  {'city_id': 8, 'city_name': 'Полярный'},
    #  {'city_id': 9, 'city_name': 'Портовый'},
    #  {'city_id': 10, 'city_name': 'Приморский'},
    #  {'city_id': 11, 'city_name': 'Садовый'},
    #  {'city_id': 12, 'city_name': 'Северный'},
    #  {'city_id': 13, 'city_name': 'Степной'},
    #  {'city_id': 14, 'city_name': 'Таёжный'},
    #  {'city_id': 15, 'city_name': 'Центральный'},
    #  {'city_id': 16, 'city_name': 'Южный'}]


def get_city_data(city_id):
    r = requests.get('http://dt.miet.ru/ppo_it/api/' + city_id,
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    # Тут вроде понятно
    house_count = r.json()['data']['house_count']
    area_count = r.json()['data']['area_count']
    apartment_count = r.json()['data']['apartment_count']
    temperature = r.json()['data']['temperature']
    city_name = r.json()['data']['city_name']
    print(house_count, area_count, apartment_count, temperature, city_name)


def get_city_temperature(city_id):
    r = requests.get('http://dt.miet.ru/ppo_it/api/' + city_id + '/temperature',
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    # Тут тоже вроде понятно
    temp = r.json()['data']
    print(temp)


def get_area_data(city_id, area_id):
    r = requests.get('http://dt.miet.ru/ppo_it/api/' + city_id + '/' + area_id,
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    # Возвращает массив со словарями, в которых содержатся id домов и их кол-во квартир (В районе)
    # {'house_id': 1, 'apartment_count': 56} и т. д.
    print(r.json()['data'])


def get_apartment_count(city_id, area_id, house_id):
    r = requests.get('http://dt.miet.ru/ppo_it/api/' + city_id + '/' + area_id + '/' + house_id,
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    # Возвращает количество квартир в доме в районе в городе ¯\_(ツ)_/¯
    apartment_count = r.json()['data']
    print(apartment_count)


def get_apartments_temperature(city_id, area_id, house_id):
    r = requests.get('http://dt.miet.ru/ppo_it/api/' + city_id +
                     '/' + area_id + '/' + house_id + '/temperature',
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    # Возвращает массив со словарями, в которых квартиры и температура в них
    # {'apartment_id': 1, 'temperature': 19} и т. д.
    print(r.json()['data'])


def get_apartment_temperature(city_id, area_id, house_id, apartment_id):
    r = requests.get('http://dt.miet.ru/ppo_it/api/' + city_id + '/' +
                     area_id + '/' + house_id + '/' + apartment_id,
                     headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    # Возвращает температуру в квартире в доме в районе в городе
    temp = r.json()['data']['temperature']
    print(temp)


# Здесь должна быть функция, но её тут нет, т.к. она бесполезна
