def isprime(number):
  flag = 0
  for i in range(2,number):
    if number%2==0:
     flag = 1
    else:
      flag = 0
  if flag == 0:
    return 'prime'
  else:
    return 'not prime'

print(isprime(3))