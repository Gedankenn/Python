import time
import sys
sys.setrecursionlimit(100000)


def iterativo_fibonacci(num):
	atual=1
	anterior=1
	proximo=1
	for i in range(0,num):
		proximo=atual+anterior
		anterior=atual
		atual=proximo
	return proximo


def recursivo_fibonacci_dinamico(list,num):
	if list[num]!= -1:
		return list[num]
	if num<=1:
		return 1
	else:
		list[num]=recursivo_fibonacci_dinamico(list,num-1)+recursivo_fibonacci_dinamico(list,num-2)
		return list[num]



def fast_fibonacci(list,num):
	if list[num]!=-1:
		return list[num]
	if num<=2:
		return 1
	k=num//2
	a=fast_fibonacci(list,k+1)
	b=fast_fibonacci(list,k)
	ans=0
	if num%2==1:
		ans=(a*a)+(b*b)
	else:
		ans=b*(2*a-b)
	list[num]=ans
	return ans

f=open("fibonacci.txt","a")

f.write("tamanho, tempo_iterativo, tempo_dinamico, tempo_fast\n")

for num in range(100,4001,100):
	list=[-1 for i in range(num+1)]

	f.write('%d'", "%num)
	#iterativo
	Ti=time.clock()
	iterativo_fibonacci(num)
	Tf=time.clock()
	f.write('%f'", "%(Tf-Ti))

	#recursivo dinamico
	Ti=time.clock()
	recursivo_fibonacci_dinamico(list,num)
	Tf=time.clock()
	f.write('%f'", "%(Tf-Ti))


	#fast fibonacci
	list=[-1 for i in range(num+1)]
	Ti=time.clock()
	fast_fibonacci(list,num)
	Tf=time.clock()
	f.write('%f'","%(Tf-Ti))
	f.write("\n")

