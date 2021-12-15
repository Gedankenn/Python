import random

def soma(list,inicio,fim):
	if fim-inicio==1:
		return list[fim]+list[inicio]
	if fim-inicio==0:
		return list[inicio]
	else:
		meio=(inicio+fim)//2
		v1=soma(list,inicio,meio)
		v2=soma(list,meio+1,fim)
		return v1+v2

lista=random.sample(range(10),3)
print(lista)
print(soma(lista,0,2))