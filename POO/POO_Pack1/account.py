# Account Super Class

# Classes
class Account:
    # Constructor
    def __init__(self, agency, agency_dig, code, account_number, account_dig, balance):
        self.__agency=agency
        self.__agency_dig=agency_dig
        self.__code=code
        self.__account_number=account_number
        self.__account_dig=account_dig
        self.__balance=balance

    # Getters

    @property
    def agency(self):
        return self.__agency

    @property
    def agency_dig(self):
        return self.__agency_dig

    @property
    def code(self):
        return self.__code

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_dig(self):
        return self.__account_dig

    @property
    def balance(self):
        return self.__balance

    # Setters

    @agency.setter
    def agency(self, agency):
        self.__agency = agency

    @agency_dig.setter
    def agency_dig(self, agency_dig):
        self.__agency_dig = agency_dig

    @code.setter
    def code(self, code):
        self.__code = code

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # Show Account Informations
    def __str__(self):
        return (
            f"Agencia: {self.__agency}-{self.__account_dig}\n"
            f"Código do banco: {self.__code}\n"
            f"Número da conta: {self.__account_number}-{self.__account_dig}\n"
            f"Saldo: {self.__balance}"
        )

# Instances
account=Account(1234, 5, 131, 152437, 9, 235.87)

# Exit
print(account)