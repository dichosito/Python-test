import sys

def Fibonacci(n):
        if n<0:
           sys.exit("El numero ingresado no es positivo")
        else:    
           a=1
           b=1
           if n==1:
              print('0')
           elif n==2:
              print('0','1')
           else:
              for i in range(n-3):
                total = a + b
                b=a
                a=total
           print("Del número ",n,"su fibonacci es",total)
                                      
Fibonacci(-200)
