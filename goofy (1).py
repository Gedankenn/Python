num_digitos = int(input(""))
num_remover = int(input(""))

vetor = list(range(0,num_digitos))
novo_vetor = list(range(0,num_remover))
for i in range(0,num_digitos):
	vetor[i]=int(input(""))

aux2=num_remover
cont=0
cont2=0
cont3=0

for cont in range(cont,aux2):
	maior=0
	for cont2 in range(cont2,num_digitos - num_remover + 1):
		if vetor[cont2] > maior:
			maior = vetor[cont2]
			aux=cont2

	novo_vetor[cont3]=maior
	cont3=cont3+1
	num_remover=num_remover-1
	cont2=aux+1


print(novo_vetor)

