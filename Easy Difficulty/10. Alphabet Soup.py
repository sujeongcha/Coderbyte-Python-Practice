#Have the function AlphabetSoup(str) take the str string parameter being passed and 
#return the string with the letters in alphabetical order (ie. hello becomes ehllo). 
#Assume numbers and punctuation symbols will not be included in the string.

#My Solution
def AlphabetSoup(str):
  sorted_list = sorted(list(str))
  result = "".join(sorted_list)
  return result
