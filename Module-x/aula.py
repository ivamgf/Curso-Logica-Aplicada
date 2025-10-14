# Aula
# Tema: Loop, if

# Declarações
alunos = []
notas = []
MEDIA = 6.0
MINIMO = 3.0

for i in range(5):
    # Entradas
    aluno = input("Digite o nome do aluno:")
    nota = float(input("Digite a nota do aluno:"))

    alunos.append(aluno)
    notas.append(nota)

    if(float(nota)>=MEDIA):
        print(f"O aluno está APROVADO com nota {nota}")
    elif(float(nota)>=MINIMO):
        print(f"O aluno está RECUPERAÇÃO com nota {nota}")
    else:
        print(f"O aluno está REPROVADO com nota {nota}")

print(alunos)
print(notas)
