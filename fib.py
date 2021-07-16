def fibanocci(n):#fibnocci number at index
	if n<0:	
		print("Incorrect input")
	elif n==0:
		return 0
	elif n==1 or n==2:
		return 1
	else:
	   return fibanocci(n-1)+fibanocci(n-2)
	   
print(fibanocci(9))
		
