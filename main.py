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

#===Instructions===#
print("""
 __      __          _    ___                
 \ \    / /__ _ _ __| |  / __|_  _ ___ ______
  \ \/\/ / _ \ '_/ _` | | (_ | || / -_|_-<_-<
   \_/\_/\___/_| \__,_|  \___|\_,_\___/__/__/
                                                                   
""")
print("Welcome to Word Guess!")
print("You will be prompted to guess a letter to discover the secret word.")
print("However, you have 5 strikes! Guess incorrectly and you will gain a strike!")
print("Good luck!")
print()
  
#===Variables===#
#SECRET WORD
secret = "Spyhnx"
secret = secret.upper() #Just incase someone changes secret and does not make it all caps

#List of Guesses
guesses = []

#Number of strikes (default value)
strikes = 0

#===The Game Loop===#
while strikes < 5 and not hasWon(secret, guesses):

  #Step 1: Prompt for a guess
  guess = getGuess()
  guesses.append(guess)
  
  #Step 2: Check if guess is in the secret word
  if guess in secret:
    #If the guess is in the secret word, show the user where
    displaySecret(secret, guesses)
    print()

  else:
    #If the guess is not in the secret, add a strike and tell the user
    strikes += 1
    print(f"{guess} is not in the word. You have {strikes}/5 strikes.")

#Tell the user if they won or not
if hasWon(secret, guesses):
  print("""
  ◝(ᵔᵕᵔ)◜
  """)
  print("Congratulations! You won!")
else:
  print("""
  ( • ᴖ • ｡)
  """)
  print("Sorry, better luck next time!")

