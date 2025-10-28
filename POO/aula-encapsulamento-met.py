# Aula - Encapsulamento de Métodos Privados

# Classes
class Pessoa():
    # Constructor
    def __init__(self, name, cpf, dt_birth, address, address_number, phone):
        # Private Atributes (__)
        self.__name=name
        self.__cpf=cpf
        self.__dt_birth=dt_birth
        self.__address=address
        self.__address_number=address_number
        self.__phone=phone

   # Get name
    def getName(self):
        return self.__name

    # Set name
    def setName(self, name):
        self.__name = name

# Instances
pessoa=Pessoa("João", 12345678901, "12/08/1980", "Rua das amoras", 16, "55+ (48) 9 2837-2746")
pessoa.setName("Roberto")
pessoa_name=pessoa.getName()

# Exit
print(pessoa_name)