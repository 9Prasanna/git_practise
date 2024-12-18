def print_square():
  number = int(input("Enter the number to square: "))
  if number <0:
      number = abs(number)
  return number**2
print(print_square())