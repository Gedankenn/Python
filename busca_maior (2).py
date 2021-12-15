import random


def busca_binaria(list, init, end):
	if end - init <= 1:
		if init>end:
			return list[init]
		else:
			return list[end-1]
	else:
		m=(init+end)//2
		v1=busca_binaria(list,init,m)
		v2=busca_binaria(list,m+1,end)
		if v1>v2:
			return v1
		else:
			return v2


lista2=random.sample(range(10),10)
print(lista2)
print(busca_binaria(lista2,0,10))