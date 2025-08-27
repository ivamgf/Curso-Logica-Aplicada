# Exercício 1 - Lista 1
# 1. Criar um algoritmo para ler os lados de um triângulo e identificar se é equilátero.

# Declarations
unidade = input("Digite a unidade utilizada:")
lado_a = input("Digite o valor inteiro da medida do lado a:")
lado_b = input("Digite o valor inteiro da medida do lado b:")
lado_c = input("Digite o valor inteiro da medida do lado c:")

# Validations
if(int(lado_a) == int(lado_b)):
    if(int(lado_a) == int(lado_c)):
        if(int(lado_b) == int(lado_c)):
            print(f"O triângulo é equilátero e seus lados tem medida de {lado_a} {unidade}")
else:
    print("O triângulo não é equilátero!")