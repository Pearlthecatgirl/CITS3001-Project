#!/usr/bin/python3
from random import randint
clues=500
sus=500
cl=[[randint(0, clues+sus)] for _ in range(clues)]

tup=lambda clues, sus, m: (clues+sus-1, randint(-100,100), randint(0,100), randint(0, 100))
t=lambda m:tup(clues,sus,m)
for i in range(len(cl)):
    for j in range(cl[i][0]-1):
        x=t(j)
        while x[0]==j:
            x=t(j)
        cl[i].append(t(j))
print(cl)

