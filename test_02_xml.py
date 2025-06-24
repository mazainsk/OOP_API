# Дан xml-файл с новостями. Нужно написать функцию read_json, которая будет возвращать список самых часто
# встречающихся в новостях слов не меньше определенной длины. По умолчанию минимальная длина слова более 6 символов,
# а количество слов - 10. Приведение к нижнему регистру не требуется.
#
# В результате корректного выполнения задания будет выведен следующий результат:
# ['туристов', 'компании', 'Wilderness', 'странах', 'туризма', 'которые', 'африканских', 'туристы', 'является', 'природы']

import xml.etree.ElementTree as ET
from collections import Counter


def read_xml(file_path, word_min_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    with open(file_path, encoding='UTF-8') as f:
        parser = ET.XMLParser(encoding='UTF-8')
        tree = ET.parse(f, parser)
        root = tree.getroot()
        descriptions_list = root.findall('channel/item/description')
        all_words = (' '.join([item.text for item in descriptions_list])).split()
        words_with_criteria = [word for word in all_words if len(word) > word_min_len]
        words_freq = Counter(words_with_criteria).most_common(10)
    return [item[0] for item in words_freq]

if __name__ == '__main__':
    print(read_xml('newsafr.xml'))