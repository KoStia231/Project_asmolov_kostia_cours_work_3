class Transfer:
    def __init__(self, date, amount, amount_name, description, to_transaction, from_transaction):
        """инициализация"""
        self.date = date
        self.amount = amount
        self.amount_name = amount_name
        self.description = description
        self.to_transaction = to_transaction
        self.from_transaction = from_transaction

    def get_card_number(self):
        """возвращает карту в шифровонном виде"""
        card_name = self.from_transaction.split()[:-1]
        card_number = self.from_transaction.split(-1)
        result = f'{" ".join(card_name)} {card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}'
        return result

    def get_bank_number(self):
        """возвращает номер счета в шифровонном виде"""
        _name = self.to_transaction.split()[:-1]
        _number = self.to_transaction.split(-1)
        result = f'{" ".join(_name)} ** {_number[-4:]}'
        return result

    def get_description(self):
        """возвращает описание перевода"""
        return self.description

    def get_amount(self):
        """возвращает сумму перевода"""
        return self.amount

    def get_amount_name(self):
        """возвращает валюту перевода"""
        return self.amount_name

    def get_data(self):
        """возвращает дату точно также как и в исходном .json"""
        return self.date
