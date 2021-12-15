a=int(input(""))
b=int(input(""))
c=int(input(""))

delta=b*b - (4*a*c)
i=0.00001
if delta<0:
	print("nao possui rais real")
else:
	while (i*i) < delta:
		i=i+0.00001
	x1=(-b-i)/(2*a)
	x2=(-b+i)/(2*a)

	print("as raises sao: x1=%.2f x2=%.2f"%(x1, x2))