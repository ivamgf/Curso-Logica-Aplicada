# Client Class

# Classes
class Client:
    # Constructor
    def __init__(self, name, cpf, address, address_number, phone, email):
        # Privates Atributes
        self.__name=name
        self.__cpf=cpf
        self.__address=address
        self.__address_number=address_number
        self.__phone=phone
        self.__email=email

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def address(self):
        return self.__address

    @property
    def address_number(self):
        return self.__address_number

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    # Setters

    @name.setter
    def name(self, name):
        self.__name=name

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf=cpf

    @address.setter
    def address(self, address):
        self.__address=address

    @address_number.setter
    def address_number(self, address_number):
        self.__address_number = address_number

    @phone.setter
    def phone(self, phone):
        self.__phone=phone

    @email.setter
    def email(self, email):
        self.__email=email

    # show client informations
    def __str__(self):
        return (f"Cliente: {self.__name}\n"
                f"CPF: {self.__cpf}\n"
                f"Endereço: {self.__address}, {self.__address_number}\n"
                f"Telefone: {self.__phone}\n"
                f"E-mail: {self.__email}")

# Instances
client = Client("João", 12345678901, "Rua das amoras", 16, "55+ (48) 9 2837-2746", "joao@gmail")

# Exit
print(client.name)
print(client.cpf)
print(client.address)
print(client.address_number)
print(client.phone)
print(client.email)
print(client)


