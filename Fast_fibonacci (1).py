#Fast fibonacci
import time
import sys
sys.setrecursionlimit(10000)

def Fast_fibonacci(list, num):
	if list[num]!=-1:
		return list[num]
	if num<=2:
		return 1
	k=num//2
	a=Fast_fibonacci(list,k+1)
	b=Fast_fibonacci(list,k)
	ans=0
	if num%2==1:
		ans=(a*a)+(b*b)
	else:
		ans=b*(2*a-b)
	list[num]=ans
	return ans

entrada=int(input(""))
list=[-1 for i in range(0,entrada+1)]
Ti=time.clock()
print(Fast_fibonacci(list,entrada))
Tf=time.clock()
print( )
print(Tf-Ti)