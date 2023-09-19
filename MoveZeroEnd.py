def move_zero(l):
	res=[]
	c=0
	for i in range(len(l)):
		if l[i]>0:
			res.append(l[i])
		else:
			c+=1
	for i in range(c):
		res.append(0)
	print(res)
	
l=[0,1,0,3,12]
move_zero(l)