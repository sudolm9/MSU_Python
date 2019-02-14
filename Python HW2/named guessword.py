#Maciej Sudol
#named guessword
#This program picks a random word and lets the user guess letters and prints the word after a few tries

def guessword():
  import random
  words = ['montclair', 'csit', 'university', 'wednesday', 'march', 'college', 'computer',
           'lab', 'kite', 'summer', 'semester', 'advisor', 'mouse', 'keyboard', 'yawn',
           'blue', 'ocean', 'beach', 'powerpoint', 'google']
  word = random.choice(words)

  letter_number = len(word)
  print("The number of letters in the word is", letter_number)

  l = input("Guess a letter: ")
  
  if word.count(l) == 0:
    print("No luck!")
  else:
    print("Found the letter!")
    print(word)
   
   
    
    

          
