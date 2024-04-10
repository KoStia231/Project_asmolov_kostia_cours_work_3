import json


def get_data(file_name) -> list:
    """читает файл json, конвертирует в лист с словарями и взовращает его"""
    with open(file_name, 'r', encoding="utf-8") as file:
        json_ = file.read()
        json_list = json.loads(json_)
    return json_list
