#Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. 
#Words will be separated by only one space.

#My Solution
def LetterCapitalize(str):
  splitted = str.split()
  result = ''
  for word in splitted:
    result += word[0].upper()+word[1:]+' '
  return result
  
#Best Solution
def LetterCapitalize(str): 
  if str.istitle():
    return str
  else:
    return str.title()
