def findSum(n):
	sum=0
	x=1
	while(n>0):
		sum=sum+n
		n=n-1
	return sum
n=int(input("ENTER A NUM:"))
print findSum(n)
