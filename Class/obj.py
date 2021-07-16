class Q:
      def __init__(self):
	   self.a=S()
	   self.b=S()
      def e(self,n):
	   self.a.push(n)
      def d(self):
	  if len(self.b) == 0:
	      while len(self.a) > 0:
		self.b.push(self.a.pop())

	  return self.b.pop()

