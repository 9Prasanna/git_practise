
# code modification has been done 
# changes that are made are removing the flag and making it as simple by providing the return statement directly
def isprime(number):
  for i in range(2,number):
    if number%2==0:
      return 'not prime'
    else:
      return 'prime'

print(isprime(3))
