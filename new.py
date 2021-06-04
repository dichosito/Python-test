import numpy as np
import numpy.linalg as LA
N = 1000 #No. de vectores aleatorios
p = 3 #Dimension de matriz y vectores
A = np.array([[1,2,3],
              [4,5,6]])
print(A)
def estimar_norma_mat(A,p,N):    # estimar norma p de matriz A usando N vectores aleatorios
    y = np.zeros(N)       # vector para almacenar el cociente entre las normas de vectores
       
    for i in range(N):        
        # escribe tu codigo aqui
        vector = np.random.randn(p)
        if i < 11:
            print("N",i,vector)
        if i > N-10:
            print("N",i,vector)
        norma = LA.norm(A@vector,np.inf)/ LA.norm(vector,np.inf)
        y[i-1] = norma

    #print (y) 
    print ("Maximo",np.max(y))
    ordenes = [1,2,np.inf]
    aproximado = [LA.norm(y,orden) for orden in ordenes]
    real = [LA.norm(A,orden) for orden in ordenes]

    print(f"{'':11}|{'||A||1':-^20}|{'||A||2':-^20}|{'||A||oo':-^20}")
    print("|".join(["Aproximado "]+[f"{x:20}" for x in aproximado]))
    print("|".join(["Exacto     "]+[f"{x:20}" for x in real]))
    
    return 

# ejecuta tu codigo aqui
estimar_norma_mat(A,p,N)


