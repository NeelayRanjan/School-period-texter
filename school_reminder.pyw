from twilio.rest import Client
from datetime import datetime
import time as clock

monday = ['07:25', '08:03', '08:40', '09:18', '09:55', '10:33', '11:10', '11:47']
regular = ['07:25', '08:40', '09:55', '11:10']
s = ['Digital Electronics', 'Precalculus', 'Honors Blended Chemistry', 'Spanish 3', 'English 2', 'Lunch', 'PE',
     'Principles of Engineering']
client = Client("login", "login")


def startClass(period):
    client.messages.create(to="myphonenumber", from_="twilionumber", body=period + " will start soon.")


while True:
    while datetime.now().strftime('%A').lower() == 'monday':
        time = datetime.now().strftime('%H') + ':' + datetime.now().strftime('%M')
        if time == monday[0]:
            startClass(s[0])
        elif time == monday[1]:
            startClass(s[1])
        elif time == monday[2]:
            startClass(s[2])
        elif time == monday[3]:
            startClass(s[3])
        elif time == monday[4]:
            startClass(s[4])
        elif time == monday[5]:
            startClass(s[5])
        elif time == monday[6]:
            startClass(s[6])
        elif time == monday[7]:
            startClass(s[7])
        clock.sleep(60)

    while datetime.now().strftime('%A').lower() == 'tuesday' or datetime.now().strftime('%A').lower() == 'thursday':
        time = datetime.now().strftime('%H') + ':' + datetime.now().strftime('%M')
        if time == regular[0]:
            startClass(s[0])
        elif time == regular[1]:
            startClass(s[1])
        elif time == regular[2]:
            startClass(s[2])
        elif time == regular[3]:
            startClass(s[3])
        clock.sleep(60)

    while datetime.now().strftime('%A').lower() == 'wednesday' or datetime.now().strftime('%A').lower() == 'friday':
        time = datetime.now().strftime('%H') + ':' + datetime.now().strftime('%M')
        if time == regular[0]:
            startClass(s[4])
        elif time == regular[1]:
            startClass(s[5])
        elif time == regular[2]:
            startClass(s[6])
        elif time == regular[3]:
            startClass(s[7])
        clock.sleep(60)
