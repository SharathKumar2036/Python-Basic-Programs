from __future__ import print_function
n=int(input("Enter a number :"))
a=0
b=1
count=1
sum=0
print("Fibanocci Series:",end=' ')
while(count<=n):
	print(sum,end = ' ')
	count +=1
	a=b
	b=sum
	sum=a+b

