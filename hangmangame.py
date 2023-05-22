#i added this to randomly pick any word from a list
import random

#the secret word the player is trying to guess

food_list = ["soda", "pizza", "fries", "chicken", "nuggets", "eggs", "bacon", "cake", 
             "sweets", "yogurt", "potatoes", "oranges", "grapes", "apples", "peaches", 
             "oats", "nuts", "avacado", "pears", "bananas", "lemon", "cornflakes"]
secretword = f"{random.choice(food_list)}"
letterguessed = ""

#the number of turns before the player loses
failurecount = 6

#Loop until the player has made too many failed attempts
#Will 'break' loop if they suceed instead
while failurecount > 0:
    
    #get the guessed letter from the player
    the_guess = input(" Enter a letter: ")


    if the_guess in secretword:

        #player guessed the letter correctly
        print(f"Correct. The letter {the_guess} is in the word.")
    else:

        #player guessed the the letter incorrectly
        failurecount -= 1
        print(f"Incorrect. There are no {the_guess} in the secret word. You currently have {failurecount} turn(s) to go.")
    
    #Maintain a list of all the letters guessed
    letterguessed = letterguessed + the_guess
    wronglettercount = 0

    for letter in secretword:
        if letter in letterguessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wronglettercount += 1
    
    #if there were no wrong letters, the player won
    if wronglettercount == 0:
        print(f" Congratulations! The secret word was: {secretword}. You Won!!!")
        break
    #if the user is all out of turns
else:
    print(f" Sorry, you guessed this incorrectly. the word was {secretword}.")

#by the best RoDidDat#
