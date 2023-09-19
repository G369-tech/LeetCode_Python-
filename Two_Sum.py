def Two_Sum(nums,target):
	res=[]
	n=0
	for i in range(0,len(nums)):
		for j in range(1,len(nums)):
			if nums[i]+nums[j]==target:
				a,b=i,j
				res.append(a)
				res.append(b)
				n=1
		if n==1:
				break
				
				
	print(res)
	
nums=[2,7,11,15]
target=9
Two_Sum(nums,target)
