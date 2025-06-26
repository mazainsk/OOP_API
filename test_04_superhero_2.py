# Тренажёр, задание «Кто самый умный супергерой (часть 2)».
# Необходимо написать функцию для определения самого умного супергероя среди списка супергероев.
# API с информацией по всем супергероям: https://akabab.github.io/superhero-api/api

import requests


# 1й вариант: с несколькими GET-запросами (по количеству ID, передаваемых в функцию).
def get_the_smartest_superhero_1(superheroes) -> str:
    url = 'https://akabab.github.io/superhero-api/api'
    heroes = []
    for hero_id in superheroes:
        resp = requests.get(f'{url}/id/{str(hero_id)}.json').json()
        heroes.append((resp['name'], resp['powerstats']['intelligence'], hero_id))
    the_smartest_superhero = sorted(heroes, key=lambda x: (-x[1], x[2]))[0][0]
    return the_smartest_superhero

# 2й вариант: с одним GET-запросом, но с перебором всех героев в JSON-словаре.
def get_the_smartest_superhero_2(superheroes) -> str:
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url).json()
    heroes = []
    for hero in resp:
        if hero['id'] in superheroes:
            heroes.append((hero['name'], hero['powerstats']['intelligence'], hero['id']))
    the_smartest_superhero = sorted(heroes, key=lambda x: (-x[1], x[2]))[0][0]
    return the_smartest_superhero


searching_ids = [1, 7, 4]
print(get_the_smartest_superhero_1(searching_ids))
print(get_the_smartest_superhero_2(searching_ids))