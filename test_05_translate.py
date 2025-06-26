# Тренажёр, задание «Переводчик».
# Необходимо написать функцию, которая принимает русское слово и возвращает его перевод на английском языке.
# Описание API: https://yandex.ru/dev/dictionary/

import requests
from api_keys import yandex_key
from pprint import pprint

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'  # Для ответа в форме JSON


def translate_word(word):
    params = {
        'key': yandex_key,
        'lang': 'ru-en',
        'text': word,
        'ui': 'ru',
        'flags': 0
    }
    resp = requests.get(url, params=params)
    # pprint(resp.json())  # Можно посмотреть всю структуру и вытащить все значения слова.
    trans_word = resp.json()['def'][0]['tr'][0]['text']
    return trans_word


if __name__ == '__main__':
    # word = 'машина'
    # assert translate_word(word) == 'car'
    print(translate_word('фиолетовый'))