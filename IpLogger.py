#import datetime 
#from playsound import playsound

#hour = int(input("Enter hour: "))
#minute = int(input("Enter minute: "))
#am_pm = input("am/pm: ")

#if am_pm == "pm":
#    hour = hour + 12

#while True:
#    if hout == datetime.datetime.now().hour and minute == datetime.datetime.now().minute:
#        print("Alarm ON!")
#        playsound("alarm.mp3")
#        break
   
import socket 

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

print('My IP Address is:' + ipAddress)

