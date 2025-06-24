# Дан json-файл с новостями. Нужно написать функцию read_json, которая будет возвращать список самых часто
# встречающихся в новостях слов не меньше определенной длины. По умолчанию минимальная длина слова более 6 символов,
# а количество слов - 10. Приведение к нижнему регистру не требуется.
#
# В результате корректного выполнения задания будет выведен следующий результат:
# ['туристов', 'компании', 'Wilderness', 'странах', 'туризма', 'которые', 'африканских', 'туристы', 'является', 'природы']

import json
from collections import Counter


def find_values_by_key(json_data, key_to_find):
    """
    Функция рекурсивного поиска в JSON-структуре всех значений по заданному ключу.
    """
    values = []
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == key_to_find:
                values.append(value)
            elif isinstance(value, (dict, list)):
                values.extend(find_values_by_key(value, key_to_find))
    elif isinstance(json_data, list):
        for item in json_data:
            values.extend(find_values_by_key(item, key_to_find))
    return values

def read_json(file_path, word_min_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    with open(file_path, encoding='UTF-8') as f:
        json_data=json.load(f)
        description_values = find_values_by_key(json_data, 'description')
        all_words = (' '.join(description_values)).split()
        words_with_criteria = [word for word in all_words if len(word) > word_min_len]
        words_freq = Counter(words_with_criteria).most_common(10)
    return [item[0] for item in words_freq]


if __name__ == '__main__':
    print(read_json('newsafr.json'))