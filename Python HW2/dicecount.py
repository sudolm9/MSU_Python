#Maciej Sudol
#dicecount
#This program simulates the rolling of a dice and ouputs the average

def diceroll():
  import random
  
  runs = 50
  total = 0

  
  for i in range(1,runs+1):
    d = random.randint(1,6)
    total = total + d
    
    print(d)
    
  print("Average of the rolls was: ", total/runs)


  
  
  

