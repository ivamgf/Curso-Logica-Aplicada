# main.py

# Imports
from client import Client
from account import Account
from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount

# Instanciar Cliente
client = Client(
    name="João",
    cpf=12345678901,
    address="Rua das Amoras",
    address_number=16,
    dt_birth="12/02/1980",
    phone="55+ (48) 9 2837-2746",
    email="joao@gmail"
)

# Instanciar Conta Corrente
checkingAccount = CheckingAccount(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=152437,
    account_dig=9,
    balance=235.87
)

# Instanciar Conta Poupança
savingsAccount = SavingsAccount(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=27653,
    account_dig=5,
    balance=150.89
)

# Exibir informações
print("=== DADOS DO CLIENTE ===")
print(client)

print("\n=== CONTA CORRENTE ===")
print(checkingAccount)

print("\n=== CONTA POUPANÇA ===")
print(savingsAccount)
