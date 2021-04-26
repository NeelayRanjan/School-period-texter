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
        try:
            startClass(s[monday.index(datetime.now().strftime('%H') + ':' + datetime.now().strftime('%M'))])
        except ValueError:
            pass
        clock.sleep(60)

    while datetime.now().strftime('%A').lower() == 'tuesday' or datetime.now().strftime('%A').lower() == 'thursday':
        try:
            startClass(s[regular.index(datetime.now().strftime('%H') + ':' + datetime.now().strftime('%M'))])
        except ValueError:
            pass
        clock.sleep(60)

    while datetime.now().strftime('%A').lower() == 'wednesday' or datetime.now().strftime('%A').lower() == 'friday':
        try:
            startClass(s[regular.index(datetime.now().strftime('%H') + ':' + datetime.now().strftime('%M')) + 4])
        except ValueError:
            pass
        clock.sleep(60)
