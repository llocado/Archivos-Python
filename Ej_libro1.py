from datetime import datetime
import time
import random

odds= []

for i in range (1,60,2):
    odds.append(i)

for i in range (5):
    right_this_minute=datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        print("Not an odd minute")
    wait_minute=random.randint(1,60)
    time.sleep(wait_minute)

