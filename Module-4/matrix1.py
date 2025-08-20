# Matrix

# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos
print(matriz[0][0])  # 1 (linha 0, coluna 0)
print(matriz[1][2])  # 6 (linha 1, coluna 2)

# Alterando elemento
matriz[2][1] = 99
print(matriz)

# Criando matriz 3x3 preenchida com zeros
linhas = 3
colunas = 3
matriz = [[0 for j in range(colunas)] for i in range(linhas)]

print(matriz)

import numpy as np

# Criando matriz 3x3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matriz)

# Operações
print(matriz.shape)    # (3, 3) → 3 linhas e 3 colunas
print(matriz[1, 2])    # 6
print(matriz.T)        # transposta
print(matriz * 2)      # multiplicação por escalar
