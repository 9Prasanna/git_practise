class hello:
  def __init__(self,first_number,second_number):
      while True:
          choose =input("which operation you want to perform 1.Addition\n2.subtraction\n3.multiplication\n4.floordiv\n5.Truediv\n6.power\n7.modlus\n")
          if choose == '1':
            self.add(first_number,second_number)
          elif choose=='2':
            self.sub(first_number,second_number)
          elif choose=='3':
            self.muli(first_number,second_number)
          elif choose=='4':
            self.floordiv(first_number,second_number)
          elif choose=='5':
            self.truediv(first_number,second_number)
          elif choose=='6':
            self.power(first_number,second_number)
          elif choose=='7':
            self.modulus(first_number,second_number)
          else:
            break
  
  
  def add(self,first_number,second_number):
      return first_number+second_number
  
  def sub(self,first_number,second_number):
     return first_number-second_number
  def muli(self,first_number,second_number):
     return first_number*second_number
  def floordiv(self,first_number,second_number):
     return first_number//second_number
  def truediv(self,first_number,second_number):
     return first_number/second_number
  def modulus(self,first_number,second_number):
     return first_number%second_number
  def power(self,first_number,second_number):
     return first_number**second_number


a=hello(10,11)
print(a)