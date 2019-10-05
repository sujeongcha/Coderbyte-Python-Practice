#Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
#If there are two or more words that are the same length, return the first word from the string with that length. 
#Ignore punctuation and assume sen will not be empty.

#My Solution
def LongestWord(sen): 
  new = ""
  for letter in sen:
    if letter.isalpha():
      new += letter
    else:
      new += " "
  arr = new.split()
  max_word = max(arr, key=len)
  return max_word
  
#Best Solution    * str.isalpha() returns “True” if all characters in the string are alphabets
def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)
