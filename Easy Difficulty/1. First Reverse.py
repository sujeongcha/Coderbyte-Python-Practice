#Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
#For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

#My Solution
def FirstReverse(str): 
  str_r = ''
  for i in range(len(str)):
    str_r += str[-(i+1)]
  return str_r

#Best Solution (just one line!!)
def FirstReverse(str): 
  return str[::-1]
