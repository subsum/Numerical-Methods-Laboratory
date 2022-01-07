import math
#define function
def f(x):
	return (1/(x**3-3*x+2))

#function to carry out bisection method
def bisection(a,b,e):
	step=1
	condition=True
	while condition:
		c=(a+b)/2
		n=step
		print('Iteration=%d  x=%0.5f f(x)=%0.5f' % (step, c ,f(c)))
		
		if f(a)*f(c)<0:
			b=c
		else:
			a=c
		
		step=step+1
		condition = abs(f(c))>e
		if n>=(math.log(abs(b-a))-math.log(abs(e)))/math.log(2):
			print('osciallting or discontinuous')
			return 0
	print('\n Required root is: %0.5f'% c)

#input a,b,e
a=float(input('First Guess: '))
b=float(input('Second Guess: '))
e=float(input('Tolerence value: '))

#checking for correctness of initial values:IVT
if f(a) * f(b) > 0.0:
	print('Given values do not bracket the roots. Enter other values.')
else:
	bisection(a,b,e)
