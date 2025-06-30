import time

reminder = input("What should I remind you about? ")
minutes = int(input("In how many minutes? "))

time.sleep(minutes * 60)
print(f"\nReminder: {reminder}")
