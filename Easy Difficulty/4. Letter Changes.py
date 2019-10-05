#Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
#Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
#Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

#My Solution
def LetterChanges(str): 
  alphabet='AbcdEfghIjklmnOpqrstUvwxyz'
  new = ''
  for letter in str:
    if letter in alphabet.lower():
      i = alphabet.lower().find(letter.lower())
      new += alphabet[i+1]
    else: 
      new += letter
  return new

#Best Solution
def LetterChanges(str): 
    newstr = ""
    outstr = ""
    for char in str:
      if char.isalpha():
        if char != "z":
          newstr = newstr + chr(ord(char)+1)
        else:
          newstr = newstr + "a"
      else:
        newstr = newstr + char
    
    for char in newstr:
      if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
        char = char.upper()
      outstr = outstr + char
    
    return outstr
