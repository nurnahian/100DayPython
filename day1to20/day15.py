import time

timestamp = time.strftime('%H:%M:%S')

print(timestamp)

timestamp2 = int(time.strftime('%H'))
name = "Nur"

if timestamp2 <= 12 :
    print("Hi,",name,"Good morning sir")

elif timestamp2 >= 16:
    print("Hi,", name, "Good evening")

elif timestamp2 > 12:
    print("Hi", name,"Good Afternoon")

elif timestamp2 >= 20:
    print("Hi,", name, "Good night")
else:
    print("Unable to recognize the time")
