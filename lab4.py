import random
# 1.create a variable score = 0
score= 0
# 2.clear screen
while True:
    #to clear screen you can use print("\033c\033[3J", end='')
    print("\033c\033[3J", end='')

    # 3.think of a random number between 1 and 20, and display it
    #to get a random number you can use random.randint(1,20)
    myNum = random.randint(1,20)

    # 4.tell player to remember this number and wait for them to hit enter
    print(f"please remember this number:\n{myNum}")
    playerNum = input("\n please hit enter to continue....")

    # 5.clear screen
    print("\033c\033[3J", end='')

    # 6.ask player what the number was, and wait for their input
    playerNum = int(input("What was the number you just saw?"))

    # 7.if player is correct:
    if (myNum==playerNum):
        
        #increase their score
        score+=1
        #tell them they got it right, and show them their score
        print(f"Wow,you got it right 😊. Your score is {score}")
        input("\n please hit enter to continue....")
        print("\033c\033[3J", end='')
    # 8.otherwise:
    else: 
        #tell them they lose, and show their final score
        print(f"Opps, You loose 😌, your final score is {score}")
        #exit
        break
# 9.go back to step 2


