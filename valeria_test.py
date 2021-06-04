def Fibonacci(valor):
# f1= 1, f2=1
# f(n+2)=f(n+1)+fn
# n>=1 o n>0
    
    if valor>0:
        F1 = 1 #asigno el primer valor 1
        F2 = 1 #asigno el segundo valor 
        #if condicion valor de verdad o falso
        #print muestra en pantalla un resultado
        for i in range(valor -2): #bucle repetitivo for inicial y tiene fin
            tmp = F1
            F1 = F1 + F2
            F2 = tmp

        print("El Numero Fibonacci de",valor,"es",F1)
    else:
        print("el valor ingresado no es un entero positivo")

        
Fibonacci(200)
