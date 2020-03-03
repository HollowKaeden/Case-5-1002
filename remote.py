# Ваня Француз
import requests


def get_cities():
    r = requests.get('http://dt.miet.ru/ppo_it/api', headers={'X-Auth-Token': '3zqb6xwartk4fga1'})
    print(r.json())
    # {'data':
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
    #  {'city_id': 16, 'city_name': 'Южный'}]}
