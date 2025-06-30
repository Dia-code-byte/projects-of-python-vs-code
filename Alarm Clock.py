import datetime
import time
from playsound import playsound

alarm_time = input("Set alarm (HH:MM in 24-hour format): ")
alarm_hour, alarm_minute = map(int, alarm_time.split(":"))

while True:
    now = datetime.datetime.now()
    if now.hour == alarm_hour and now.minute == alarm_minute:
        print("Wake up!")
        playsound(r"C:\Users\HP\Downloads\my_name_is_chiki_uwu.mp3")
        break
    time.sleep(1)
