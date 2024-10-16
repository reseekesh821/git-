# 1.think a random number myNum between 1 and 100
# a.add the following line at the top of your code: import random
import random
print("\nHello, welcome to the number guessing game!\n")

while True:
    # b.when you need to get a random number, use the following code: myNum = random.randint(1,100)
    myNum = random.randint(1,100)

    # create a variable guess = 0
    guess= 0

    while True:
        # 2.ask player to guess a number between 1 and 100
        userResponse = input('Please enter a number between 1 to 100: ')

        # 3.if player's response is not a valid positive integer, ask again until it is,
        if not userResponse.isdecimal() or not (1 <= int(userResponse) <= 100):
            print('Oops😴, you did not enter a valid number within the range. Please try again.')
            continue  # this will skip all code below <===  

        # Ensuring the number is an valid integer and is between 1 and 100.
        userResponse = int(userResponse)
        
        # Keep track of the number of user guesses
        guess+=1

        # 4.if player's guess is less than myNum, let them know their guess is too low, then go back to step 2    
        if userResponse < myNum:
            print('Your number is too low')

        #5.if player's guess is more than myNum, let them know their guess is too high, then go back to step 2    
        elif userResponse > myNum:
            print('Your number is too high')

        # 6.otherwise, if player's guess is spot on, tell them they win!    
        else:
            print('Congratulations🎊. You guess the correct number.')
            #calucating the score where score = 10 - [number of guesses]
            score = max(10 - guess, 0) 
            print(f"Your score is: {score}")
            break

    # Asking the player if they want to play the game again, if not wrapping the code.
    play_again= input("\nDo you want to play again?: ")
    if play_again.lower() != 'yes':
       print("Thanks for playing! Good game!😍")
       break   
