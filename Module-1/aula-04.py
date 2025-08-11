# Aula 4
# Dictionary

# Dicionário de contatos
telefones = {
    "Tiago": 9199199919,
    "Diogo": 9199223948
}
# del telefones["Diogo"]

# Exibindo os contatos
print("Lista de Telefones:")
for nome, numero in telefones.items():
    print(f"{nome}: {numero}")
