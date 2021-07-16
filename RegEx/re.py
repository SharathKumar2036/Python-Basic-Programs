import re
txt="Hi there, How are you?"
x = re.search("^hi.*?$",txt)

if x:
   print("Yes!We have a match!")
else:
   print("No match")
