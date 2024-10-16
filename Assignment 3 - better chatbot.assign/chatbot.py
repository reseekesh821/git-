# CS195 - Assignment 3
# better_Chatbot

# \n is used to print the output on a new line.
# 1. asks your name.
name = input("\nWhat is your name? ").strip() # Asking for the user's name and removing any unwanted spaces using the strip function.

# 2. greets you by your name.
print(f"\nHello, {name.upper()} nice to meet you.")  # printing the user's name with capatalizing and greeting.

# 3. asks how tall you are in centimeters.
height_cm = float(input("\nHow tall you are in centimeters? ").strip())  # asking the user's height

# 4. tells you how many you's it would take to reach the moon.
# distance between earth and moon is: 384,400 km.
earth_moon_distance_cm = 384400 * 100000  # 100000 cm = 1 km.
print(f"\nOh! then, it would take approximately {earth_moon_distance_cm / height_cm:.2f} of your height to reach the moon.") # calulating the result in 2 decimal palces.

# 5. asks how much you weigh.
weight_kg_earth = float(input("\nPlease enter your weight in kilo gram! ").strip())

# 6. tells you how much you would weigh on the moon.
# moon has six times lesser gravity than the earth.
print(f"\nYou weigh approximately {weight_kg_earth / 6:.1f} kg in moon.") # caluating the result in 1 decimal palces.





