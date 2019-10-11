#Have the function SimpleSymbols(str) take the str parameter being passed and 
#determine if it is an acceptable sequence by either returning the string true or false. 
#The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a) 
#and for the string to be true each letter must be surrounded by a + symbol. 
#So the string to the left would be false. 
#The string will not be empty and will have at least one letter.

#My Solution
def SimpleSymbols(str):
  for i, char in enumerate(str):
    if char.isalpha():
      if i != 0 and str[i-1] == '+' and str[i+1] == '+':
        return 'true'
      else:
        return 'false'
