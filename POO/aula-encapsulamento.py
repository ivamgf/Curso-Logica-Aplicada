# Aula

# Classe Pessoa
class Pessoa:
    # Constructor
    def __init__(self, name, cpf, address, addressNumber, phone):
        # Private Atributes
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__addressNumber = addressNumber
        self.__phone = phone

    # Get e Set name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Get e Set cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # Get e Set address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    # Get e Set addressNumber
    @property
    def addressNumber(self):
        return self.__addressNumber

    @addressNumber.setter
    def addressNumber(self, number):
        self.__addressNumber = number

    # Get e Set phone
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone


# Instâncias
pessoa = Pessoa("João", 12345678901, "Rua das Amoras", 12, "55+ (48) 9 2837-2746")

# Modificando valores
pessoa.name = "Roberto"

# Saída
print("Nome:", pessoa.name)
print("CPF:", pessoa.cpf)
print("Endereço:", pessoa.address)
print("Número:", pessoa.addressNumber)
print("Telefone:", pessoa.phone)
