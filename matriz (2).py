import time

m=int(input(""))
n=int(input(""))


matriz=[[0 for i in range(n)] for x in range(m)]
for i in range(m):
	for j in range(n):
		matriz[i][j]=float(input(""))
	j=0

i=0
j=0
for i in range(m):
	print(matriz[i])

print( )

i=1
aux=0;
aux2=0
for j in range(m-1):
	i=aux
	while(i<n-1):
		if(matriz[aux][j]!=0):
			x=matriz[i][j]/matriz[aux][j]
			x=-x
			y=j
			while(y<n):
				matriz[i][y]=x*matriz[aux][y]+matriz[i][y]
				y=y+1
			print( )
			for aux2 in range(m):
				print(matriz[aux2])
		i=i+1
	aux=aux+1





print( )
for i in range(m):
	print(matriz[i])