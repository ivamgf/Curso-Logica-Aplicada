# Aula - Perceptron Camada simples

# Imports
import numpy as np

# Declarations
X=np.random.rand(5)
W=np.random.rand(5)
b=1
u=0

# Junção Aditiva
for i in range(len(X)):
    v=X[i]*W[i]
    u=u+v
u=u-b
print(u)

# Função de Ativação (Degrau)
if(u>=0):
    y=1
    print(f"O neurônio foi ativado com valor igual a:{y}")
elif(u<0):
    y = 0
    print(f"O neurônio foi desativado com valor igual a:{y}")