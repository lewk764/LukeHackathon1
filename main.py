#Word Guesser by Luke Rau

#Function to get a letter from the user
def getGuess():

  #Initialize variable
  guess = ""
 
  #Prompt for letter until user supplies a single letter
  while not guess.isalpha() or len(guess) != 1:
    guess = input("Enter a letter: ")

  #Return a single letter for the user's guess
  return guess.upper()

#Function to display secret word with guessed letters
def displaySecret(secret, guesses):

  #Loop through the secret word and check if a letter has been guessed
  for letter in secret.upper():
    
    if letter in guesses:
      print(letter, end=" ")

    #If the letter has not been guessed, display "_"
    else:
      print("_", end=" ")

#Function to determine if user won
def hasWon(secret, guesses):

  #Default value, will change to false if user has not guessed the word
  won = True

  #Loop through  secret word
  for letter in secret.upper():

    #if a letter is missing, set won to false
    if(letter not in guesses):

      won = False
      break

  return won
  

#Main game code

#SECRET WORD
secret = "SPHyNX"

#List of Guesses
guesses = []

#Number of Tries (default value)
tries = 0
  
#Test area
guesses.append(getGuess())
guesses.append(getGuess())
displaySecret(secret, guesses)