# Kunal Sharma IIT Jammu
# This is a simple Python script to print a greeting based on the current time of day.
# It uses the time module to get the current hour and prints a corresponding message.
import time

current_time = time.localtime()
hour = current_time.tm_hour

if 5 <= hour < 12:
    print("Good morning!")
elif 12 <= hour < 17:
    print("Good afternoon!")
elif 17 <= hour < 21:
    print("Good evening!")
else:
    print("Good night!")
