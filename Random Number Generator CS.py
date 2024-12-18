import random                                                                                                   #imports random

name = input("What is your name? ")                                                                             #asks user what is your name
print("Good luck", name)                                                                                        #tells good luck, user
rounds = 0                                                                                                  #amount of rounds
score = 0                                                                                                   #player score

while True:                                                                                                     #forever loop
    bot = random.randint(1, 10)                                                                                 #bot chooses a random number 1-10
    print(bot)
    guesses = 5                                                                                            #amount of guesses

    while guesses > 0:                                                                                            #loop as long as guess amount is greater than 0
        while True:                                                                                             #forever loop
            guess = input("The computer has chosen a number between 1 and 10. Guess that number: ")           #

            try:
               guess = int(guess)                                                                                   #not sure about this one

               if guess >= 1 and guess <= 10:
                   break
               else:
                   print("Please enter a number between 1 and 10!")
            except ValueError:
                print("Please enter a number between 1 and 10!")

        if  guess == bot:
            print("You got it!")
            score += 1
            break
        elif guess > bot:
            print("your number is too high")
        else:
            print("Your number is too low")

        guesses  -= 1
        
    rounds += 1
    
    if guesses == 0:
        print("You lost this round")
        
    while True:
        play_again = input(f"You got {score} out of {rounds} rounds. Would you like to play again? yes/no ")
        if play_again == "no":
            exit()
        elif play_again == "yes":
            break
        else:
            print("invalid response")
            
        
            
            
        
        
        
               
                    
        
               
            
