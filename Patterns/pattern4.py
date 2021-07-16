from __future__ import print_function
n=int(input("Num:"))
for i in range(n):#When value of i is 1  then in it prints one star 
	for j in range(n-i):
	    print('#',end='')
	print("\r")	
