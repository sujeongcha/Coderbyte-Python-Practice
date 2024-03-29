#Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. 
#For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
#For the test cases, the range will be between 1 and 18 and the input will always be an integer.

#My Solution
def FirstFactorial(num): 
  factor = 1
  for i in range(num):
     factor *= num-i 
  return factor
  
#Best Solution - using a function inside a function! clever!
def FirstFactorial(num): 
    if num == 1:
      return 1
    else:
      return num*FirstFactorial(num-1)
