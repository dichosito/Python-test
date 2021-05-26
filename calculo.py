def Fibonacci(n):
	if n>0:
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
				a= total
			print(total)
			 
Fibonacci(200)