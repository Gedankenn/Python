import time

def fibonacci(num):
	if num<=1:
		return 1
	return fibonacci(num-1) + fibonacci(num-2)

val=int(input(""))
Ti=time.clock()
fibonacci(val)
Tf=time.clock()
print("tempo recursivo normal: ",Tf-Ti)