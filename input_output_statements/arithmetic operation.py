class operation :
  def __init__(self,first_number,second_number):
        #  choose = input()
        #  if choose == '1':
        #     print(self.add(first_number,second_number))

    
          match input("which operation you want to perform \n1.Addition\n2.subtraction\n3.multiplication\n4.floordiv\n5.Truediv\n6.power\n7.modlus :" ):
            case '1':
                print(self.add(first_number,second_number))
            case '2':
                print(self.sub(first_number,second_number))
            case '3':
                print(self.muli(first_number,second_number))
            case '4':
                print(self.floordiv(first_number,second_number))
            case '5':
                print(self.truediv(first_number,second_number))
            case '6':
                print(self.power(first_number,second_number))
            case '7':
                print(self.modulus(first_number,second_number))
                     

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


a= operation(10,11)
