# Тренажёр, задание «Куда поедем в отпуск».
# Необходимо написать функцию, которая принимает на вход список из координат (кортеж из широты и долготы)
# и возвращает английский город. Список городов Великобритании ограничен 8 самыми популярными городами:
# Leeds, London, Liverpool, Manchester, Oxford, Edinburgh, Norwich, York.
# Гарантируется, что в списке есть как минимум 1 британский город.
# Для нахождения города по координатам рекомендуется использовать API geocode: https://geocode.maps.co/
#
# Reverse Geocode (Convert coordinates to human-readable address):
# https://geocode.maps.co/reverse?lat=latitude&lon=longitude&api_key=685db2c3bf509669253950kwj6f02ad

import requests
from time import sleep
from api_keys import geocode_key

POPULAR_UK_CITIES = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
URL = 'https://geocode.maps.co/reverse'


def find_uk_city(coordinates: list) -> str:
    for lat, lon in coordinates:
        params = {'lat': lat, 'lon': lon, 'api_key': geocode_key}
        place = requests.get(URL, params=params).json()['address']['city']
        if place in POPULAR_UK_CITIES:
            return place
        sleep(1)
    return None

if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),  # Москва
        ('52.3727598', '4.8936041'),  # Амстердам
        ('53.4071991', '-2.99168')  # Ливерпуль
    ]
#
#     assert find_uk_city(_coordinates) == 'Liverpool'

print(find_uk_city(_coordinates))