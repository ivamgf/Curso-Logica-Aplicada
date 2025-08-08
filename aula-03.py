# Aula 3
# Lists

# Imports
import datetime
from datetime import date

# Inputs
# name, birth, date_admission, salary, role, contract
list_employees = ["joao", date(1980,8,10), date(2020,3,26), 3495.34, "manager"]
list_employees.append(8374652)
# list_employees.remove(8374652)
list_stock = [23,75,24,95,90,59,87]
# list_stock.reverse()
list_stock.sort()

# Functions

# Outputs
print(list_employees)
print("Nome: ", list_employees[0])
print("Data de nascimento: ", list_employees[1])
print("Data de Admissão: ", list_employees[2])
print("Salário: ", list_employees[3])
print("Função: ", list_employees[4])
print("Contrato: ", list_employees[5])
print(list_employees.count(3495.34))
print(list_employees.index(3495.34))
print(list_stock)
# print(list_stock)