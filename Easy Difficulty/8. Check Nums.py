#Have the function CheckNums(num1,num2) take both parameters being passed and 
#return the string true if num2 is greater than num1, otherwise return the string false. 
#If the parameter values are equal to each other then return the string -1.

#My Solution
def CheckNums(num1,num2):
  if num2 == num1:
    return '-1'
  elif num2 > num1:
    return 'true'
  else:
    return 'false'
