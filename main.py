from utils.function import get_data
from utils.function import sort_status
from utils.function import sort_dates
from utils.function import revers
# from utils.function import compilation_transfer
from config import data_file_name


def __main__():
    list_data = get_data(data_file_name)
    list_sorted_status = sort_status(list_data)
    list_sorted_dates = sort_dates(list_sorted_status)
    last_5_transaction = revers(list_sorted_dates[-5:])
    for i in last_5_transaction:
        print(i)

    # l = compilation_transfer(data)
    # for i in l:
    #     # print(i.get_data())
    #     print(i.get_amount())
    #     # print(i.get_amount_name())
    #     # print(i.get_description())
    #     # print(i.get_bank_number())
    #     # print(i.get_card_number())


if __name__ == "__main__":
    __main__()
