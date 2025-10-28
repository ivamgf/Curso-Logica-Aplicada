# Aula - Criando Objetos

# Classes
class Pessoa():
    # Constructor
    def __init__(self, name, cpf, dt_birth, address, address_number, phone):
        self.name=name
        self.cpf=cpf
        self.dt_birth=dt_birth
        self.address=address
        self.address_number=address_number
        self.phone=phone

# Instances
pessoa=Pessoa("João", 12345678901, "12/08/1980", "Rua das amoras", 16, "55+ (48) 9 2837-2746")

# Exit
print(pessoa)
print(pessoa.name)
print(pessoa.cpf)
print(pessoa.dt_birth)
print(pessoa.address)
print(pessoa.address_number)
print(pessoa.phone)