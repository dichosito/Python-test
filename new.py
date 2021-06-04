import numpy as np
import numpy.linalg as la
N = 10 #1000
p= 3
A = np.array([[1,2,3],
              [4,5,6]])

def estimar_norma_mat(A,p,N):    # estimar norma p de matriz A usando N vectores aleatorios
    y = np.zeros(N)       # vector para almacenar el cociente entre las normas de vectores
    print(y)
    for i in range(N):        
        # escribe tu codigo aqui
        random = np.random.randn(p)
        print (random)
        
    return #np.max(y)

# ejecuta tu codigo aqui
estimar_norma_mat(A,p,N)

