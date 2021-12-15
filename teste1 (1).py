num = int(input("enter a numer: :"))
factorial =1

if num< 0:
	print("numero menor q 0 nao tem fatorial retardado")
elif num == 0:
	print("o fatorial de 0 e 1")
else:
	for i in range(1,num+1):
		factorial=factorial*i
	print("o fatorial de",num,"eh",factorial)