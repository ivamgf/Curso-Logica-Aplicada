# Checking Account Class

# Imports
from account import Account

# Class
class CheckingAccount(Account):
    # Constructor
    def __init__(self, agency,agency_dig,code, account_number, account_dig, balance):
        # Constructor Super Class
        super().__init__(agency,agency_dig,code)
        # Atributes Privates
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__balance = balance

    # Getters

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

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # Show Checking Account Informations
    def __str__(self):
        return (
            f"Número da conta: {self.__account_number}-{self.__account_dig}\n"
            f"Saldo: {self.__balance}"
        )

