# Тренажёр, задание «Кто самый умный супергерой (часть 1)».
# Необходимо написать функцию для определения самого умного супергероя среди Hulk, Captain America, Thanos.
# API с информацией по всем супергероям: https://akabab.github.io/superhero-api/api

import requests


def get_the_smartest_superhero() -> str:
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url).json()
    heroes = []
    for hero in resp:
        if hero['name'] in searching_names:
            heroes.append((hero['name'], hero['powerstats']['intelligence']))
    the_smartest_superhero = sorted(heroes, key=lambda x: x[1], reverse=True)[0][0]
    return the_smartest_superhero


searching_names = ['Hulk', 'Captain America', 'Thanos']
print(get_the_smartest_superhero())