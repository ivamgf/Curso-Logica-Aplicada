# Aula - Função Construtora

# Classes
class Pessoa():
    # Constructor
    def __init__(self):
        print("O objeto cliente foi criado!")
        self.name="João"
        self.cpf=12345678901
        self.dt_birth="12/08/1980"
        self.address="Rua 15 de maio"
        self.address_number=16
        self.phone="55+ (48) 9 8374-2746"

# Instances
pessoa=Pessoa()
pessoa.address_number=21

# Exit
print(pessoa)
print(pessoa.name)
print(pessoa.cpf)
print(pessoa.dt_birth)
print(pessoa.address)
print(pessoa.address_number)
print(pessoa.phone)