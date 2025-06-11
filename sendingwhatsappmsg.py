import datetime
import pywhatkit as pwk

now = datetime.datetime.now()
# Add 1 minute to current time to avoid timing issues
hour = now.hour
minute = now.minute + 1

# Adjust in case minute goes over 59
if minute >= 60:
    hour += 1
    minute = minute % 60

phone_number = "+250790732408"
message = "Hello, this is an automated test message sent using Python!"

pwk.sendwhatmsg(phone_number, message, hour, minute)
