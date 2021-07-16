class Person:#With different object instead of self
      def __init__(l,name,age):
	   l.name=name
	   l.age=age
      def myfun(abc):
	   print("Hello my age is " + abc.name +". I am " + abc.age)
p1=Person("Sharath",str(21))
p1.myfun()

