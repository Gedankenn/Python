f=open('stocks_list_2.txt','r')
f2=open('Sticks_list_3.txt','a')

for x in f:
	x=x.strip('\n')
	x=x+'.SA\n'
	f2.write(x)

f.close()
f2.close()