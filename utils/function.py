import json
import datetime


def get_data(file_name) -> list:
    """читает файл json, конвертирует в лист с словарями и взовращает его"""
    with open(file_name, 'r', encoding="utf-8") as file:
        json_ = file.read()
        json_list = json.loads(json_)
    return json_list


def sort_status(json_list: list) -> list:
    """сохраняет только операции со статусом <<EXECUTED>>"""
    result = []
    for i in json_list:
        if i.get('state') == "EXECUTED":
            result.append(i)
    return result


def sort_dates(list_: list) -> list:
    """сортирует по датам от меньшего к большему"""
    return sorted(list_, key=lambda x: x['date'])


def revers(list_: list) -> list:
    """разворачивает список от большего к меньшему"""
    return list_[::-1]


def format_date(value) -> str:
    """вернет дату в нужном виде"""
    date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime('%d.%m.%Y')


def get_from_to(dict_: dict):
    """вернет откуда карта/счет, куда карта/счет"""
    from_transaction = dict_.get("from")
    to_transaction = dict_.get("to")
    if from_transaction is None:
        return False, to_transaction
    return from_transaction, to_transaction


def cipher(str_) -> str | None:
    """возвращает номер счета в шифровонном виде или
       возвращает карту в шифровонном виде"""
    if not str_:
        return None
    elif "счет" in str_.lower():
        _name = str_.split()[:-1]
        _number = str_.split()[-1]
        result = f"{' '.join(_name)} **{_number[-4:]}"
        return result
    else:
        card_name = str_.split()[:-1]
        card_number = str_.split()[-1]
        result = f"{' '.join(card_name)} {card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"
        return result
