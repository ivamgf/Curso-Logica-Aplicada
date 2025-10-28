import numpy as np

X=np.random.rand(5)
W=np.random.rand(5)

u=0
b=1

for i in range(len(X)):
    v=X[i]*W[i]
    u=u+v
    print(u)
u=u-b

if(u>=0):
    y=1
    print(f"A rede neural foi ativada com valor de saída igual a: {y}")
elif(u<0):
    y=0
    print(f"A rede neural foi desativada com valor de saída igual a: {y}")