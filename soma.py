def soma(num):
	if num==1:
		return 1
	else:
		return soma(num-1)+num

a=int(input(""))
print(soma(a))
