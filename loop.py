import random#printing random person name in a list using loop
people=[]
x=0
while(x<8):
    person =raw_input("Enter a name:")
    people.append(person)
    x += 1

index = random.randint(0,7)

random_person = people[index]

print(random_person)






