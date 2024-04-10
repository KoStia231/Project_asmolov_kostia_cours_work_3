import json
# from utils.Transfer import Transfer


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




# def compilation_transfer(list_: list) -> list:
#     list_transfer = []
#     for i in list_:
#         list_transfer.append(Transfer(i.get('date'), i.get('operationAmount'), i.get('name'), i.get('description'),
#                                       i.get('to'), i.get('from')))
#     return list_transfer
#
