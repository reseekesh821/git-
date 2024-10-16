#CS195 - Assignment 2
#Chatbot

#1.asks your name
name=input("What is your name? ") #asking user's name and and store in the vairable 'name'

#2.greets you by your name
print(f"hello, {name} nice to meet you") # printing the user's name with some greeting.

#3.asks how tall you are inces or cm
hight_cm= float(input("how tall you are in centimeters? ")) #asking the user's height

#4.tells you how many you's it would take to reach the moon
#distance between earth and moon is: 384,400 km
earth_moon_distance_cm= 384400*1000 # 1000 cm = 1 km
me_to_reach_moon=earth_moon_distance_cm/hight_cm
print(f"Oh! then, It would take approximately {me_to_reach_moon:.2f} of your hight to reach the moon ")

#5. ask how much you weight
weight_kg_earth=float(input("Please enter your weight in kilo gram! "))
weight_in_moon= weight_kg_earth/6 #moon have six time lesser gravity than a moon
#6.tells you how much you would weigh on the moon
print(f"You weigh approximately {weight_in_moon:.1f} kg in moon")




