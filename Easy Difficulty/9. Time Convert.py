#Have the function TimeConvert(num) take the num parameter being passed and 
#return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). 
#Separate the number of hours and minutes with a colon.

#My Solution
def TimeConvert(num):
  hour = num // 60 
  minute = num - (hour*60)
  return str(hour)+':'+str(minute)
  
#Best Solution
def TimeConvert(num): 
  return ("%d:%d") % (num // 60, num % 60)
