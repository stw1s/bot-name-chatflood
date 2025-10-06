import random, time
from stuff import * #importing modules cause we need to get the lists
names = "usernamestxt.txt" #simply making files easier to get
with open(names, "r",
          encoding="utf-8") as f: 
    usernames = [line.strip() for line in f if line.strip()] #opens the 8 million username list and turns into a list
    usernames.sort(reverse=True)
lines = len(usernames)
n = 1
s = 1
numb = 1
delay = 1
print("made by stw1s\ngithub.com/stw1s")
print(f"there are, {lines} usernames in this list!")
for i in range(lines):
    print(f"{n} +rep, {usernames[i]} is {random.choice(actions)}")
    n+=1
    s+=1
    if s >= 2000:
        numberero = numb/2
        delay = delay/numberero
        s = 1
    else:
        n = n
    time.sleep(delay)
    delay = delay * 0.95
    #now this just prints out x amount names with +rep and then something
    #random after it
