import time
import sys
sys.setrecursionlimit(10000)


def fibonacci_dinamico(list, num):
	if list[num]!= -1:
		return list[num]
	if num<=1:
		return 1
	else:
		list[num]=fibonacci_dinamico(list,num-1)+fibonacci_dinamico(list,num-2)
		return list[num]

entrada=int(input(""))
list=[-1 for i in range(entrada+1)]
Ti=time.clock()
print(fibonacci_dinamico(list,entrada))
Tf=time.clock()
print( )
print(Tf-Ti)