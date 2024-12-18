
#cat
import random                                                                                           #imports random

weapons = ["rock","paper","scissors",]                                                                  #list of weapons
score = 0                                                                                               #score
score_limit = 3                                                                                         #score limit
while True:
    game_choice = str.lower(input("Do you want to play rock paper scissors or magic 8 ball? "))
    if game_choice == "rock paper scissors":
        player1_name = input("What is your name? ")                                                     #whats the player name
        while True:                                                                                     #forever loop
            play_style = str.lower(input("Do you want to play bot or two player? bot/two player "))     #asks two player or bot
            if play_style =="bot":                                                                      #if user want to play bot
                player2_name = "bot"                                                                    #player2 is bot
                break                                                                                   #breaks the code
            elif play_style =="two player":                                                             #if user wants to play 2 player
                player2_name = input("Player 2, what is your name? ")                                   #asks what is player 2's name
                break                                                                                   #breaks the code
            else:                                                                                       #else
                print("invalid response")                                                               #prints invalid response

        while score < score_limit:                                                                      #if score is less than score limit keep playing
            if play_style == "bot":                                                                     #player2 is bot
                player1 = str.lower(input("rock, paper, scissors or lightsaber?:"))                     #asks player1 rock, paper, scissors
                player2 = random.choice(weapons)                                                        #bot chooses random weapon
            else:                                                                                       #else
                player1 = str.lower(input("rock, paper, scissors or lightsaber?:"))                     #asks player1 rock, paper, scissors
                player2 = str.lower(input("rock, paper, scissors or lightsaber?:"))                     #asks player2 rock, paper, scissors

            if player1 == player2:                                                                      #if player1 is tied with player2 
                print("Sorry you tied, try again")                                                      #prints you tied
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "rock" and player2 == "paper":                                              #if player 1 is rock and player2 is paper
                print (f"{player2_name} won!")                                                          #player2 won      
                score -= 1                                                                              #minus 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "rock" and player2 == "scissors":                                           #if player 1 is rock and player2 is scissors
                print("player1 won!")                                                                   #Player1 won
                score += 1                                                                              #adds 1 to score
                print (f"{player1_name} your current score is {score}")                                 #prints player1 score
            elif player1 == "paper" and player2 == "rock":                                              #if player 1 is paper and player2 is rock
                print ("player1 won!")                                                                  #Player1 won
                score += 1                                                                              #adds 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "paper" and player2 == "scissors":                                          #if player 1 is paper and player2 is scissors
                print(f"{player2_name} won!")                                                           #player2 won
                score -= 1                                                                              #minus 1 to score
                print (f"{player1_name} your current score is {score}")                                 #prints player1 score
            elif player1 == "scissors" and player2 == "rock":                                           #if player 1 is scissors and player2 is rock
                print (f"{player2_name} won!")                                                          #player2 won
                score -= 1                                                                              #minus 1 to score
                print (f"{player1_name} your current score is {score}")                                 #prints player1 score
            elif player1 == "scissors" and player2 == "paper":                                          #if player 1 is scissors and player2 is paper
                print ("player1 won!")                                                                  #Player1 won
                score += 1                                                                              #adds 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "rock" and player2 == "paper":                                              #if player 1 is rock and player2 is paper
                print (f"{player2_name} won!")                                                          #player2 won
                score -= 1                                                                              #minus 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "lightsaber" and player2 == "rock":                                         #if player 1 is lightsaber and player2 is rock
                print ("player1 won!")                                                                  #prints player1 won
                score += 1                                                                              #adds 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "lightsaber" and player2 == "paper":                                        #if player 1 is lightsaber and player2 is paper
                print ("player1 won!")                                                                  #Player1 won
                score += 1                                                                              #minus 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "lightsaber" and player2 == "scissors":                                     #if player 1 is lightsaber and player2 is scissors
                print ("player1 won!")                                                                  #Player1 won
                score += 1                                                                              #adds 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "rock" and player2 == "lightsaber":                                         #if player 1 is rock and player2 is lightsaber
                print ("player1 won!")                                                                  #prints player1 won
                score += 1                                                                              #adds 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "paper" and player2 == "lightsaber":                                        #if player 1 is paper and player2 is lightsaber
                print ("player1 won!")                                                                  #Player1 won
                score += 1                                                                              #minus 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score
            elif player1 == "scissors" and player2 == "lightsaber":                                     #if player 1 is scissors and player2 is lightsaber
                print ("player1 won!")                                                                  #Player1 won
                score += 1                                                                              #adds 1 to score
                print(f"{player1_name} your current score is {score}")                                  #prints player1 score                                                 
            else:                                                                                       #else statement
                print("Invalid Response")                                                               #prints invalid response                       

        if score == score_limit:                                                                        #if score is equal to score limit
            #prints you win
            print(""" ___  _ ____  _                                                                
    _      _  _     
    \  \///  _ \/ \ /\  / \  /|/ \/ \  /|
     \  / | / \|| | ||  | |  ||| || |\ ||
     / /  | \_/|| \_/|  | |/\||| || | \||
    /_/   \____/\____/  \_/  \|\_/\_/  \|""")

    elif game_choice == "magic 8 ball":                                                                 #if game choice is magic 8 ball
        responses = ["Yes", "No", "Maybe", "Ask again later"]                                           #list possible responses
        question_words = ["Which", "When", "How", "Why", "Am", "Where", "Who", "Is", "What", "Whom", "Whose", "Whether"] #list possible question words
        while True:                                                                                     #forever loop
            question = input ("ask magic 8 ball anything")                                              #input ask magic 8 ball a question
            first_word = question.split()[0]                                                            #identify first word in question
            if "?" in question or first_word.capitalize() in question_words:                            #if ? or first word is capitilized
                answer = random.choice(responses)                                                       #answer is random choice of possible responses
                print("Magic 8 ball says: ", {answer})                                                  #print magic 8 ball answer
            else:                                                                                       #else
                print ("Invalid Response")                                                              #prints invalid response



    


    


    

    
