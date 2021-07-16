import random#printing random person name in a list using loop 
people=[]
people1=[]
x=0
while(x<1):
    person: object =raw_input("Enter Your last name:")
    person1 =raw_input("Enter Your first name:")
    people.append(person+person1)
    x += 1
n=int(input("enter 1 >>>> To print last name multiple times""enter 0 >>>> To print first name multiple times"))
while(n>1):
    print("Enter 0 or 1 Your prompt excluding the limit")
    n=int(input("enter 1 >>>> To print last name multiple times ""enter 0 >>>> To print first name multiple times"))
if(n==1):	
    a=int(input("Enter a number that how many times you want last name to be printed:"))
    people1.append(person*a+person1)
    g=int(input("Enter a number in how many lines that u want the same output to be printed:"))
    print("{} \n".format(people1) *g)
else:
    b=int(input("Enter a number that how many times you want first name to be printed:"))
    g=int(input("Enter a number in how many lines that u want the same output to be printed:"))
    people1.append(person+person1*b)
    print("{} \n".format(people1) *g)

    



