#1.say "Hello"
print("Hello")

#2. record user input into a variable called UserResponse.
UserResponse= input(">>")

#3. recording the user response until it is not "quit" or any capitalization of "quit" (e.g., "quiT", "Quit"): 
while UserResponse.lower() != 'quit':
    print(f"well, {UserResponse} right back at ya")
    UserResponse=input(">>")

#4. Printing the final output if the input is "quit" or any capitalization of "quit" (e.g., "quiT", "Quit"):
print("Goodbye!") 