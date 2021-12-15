def potencia(num,pot):
	if pot==0:
		return 1;
	else:
		return potencia(num,pot-1)*num

a=int(input(""))
b=int(input(""))
print(potencia(a,b))