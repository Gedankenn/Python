import random

def busca_binaria(list,chave,inicio,fim):
	if fim<inicio:
		print("numero nao encontrado")
		return 0
	else:
		meio=(inicio+fim)//2
		if list[meio]>chave:
			return busca_binaria(list,chave,inicio,meio-1)
		else:
			if list[meio]<chave:
				return busca_binaria(list,chave,meio+1,fim)
			else:
				return meio


num=int(input(""))
tam=int(input(""))
lista= random.sample(range(tam),tam)

print(busca_binaria(lista,num,0,tam))