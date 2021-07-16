n=int(input("Enter a number to check : "))
temp=n
rev=0
while(n>0):
	dig=n%10
	rev=rev*10+dig
	n=n//10
if(temp==rev):
   print("{} number is palindrome:".format(temp))
else:
   print("It is not palindrome")
