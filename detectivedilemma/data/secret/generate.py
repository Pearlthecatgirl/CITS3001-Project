#!/usr/bin/python3
from random import randint, shuffle
clues=50
sus=50
cl=[[] for _ in range(clues)]

#tup=lambda clues, sus, m: (clues+sus-1, randint(-100,100), randint(0,100), randint(0, 100))
#t=lambda m:tup(clues,sus,m)
#for i in range(len(cl)):
#    for j in range(cl[i][0]-1):
#        x=t(j)
#        while x[0]==j:
#            x=t(j)
#        cl[i].append(t(j))
#print(cl)

for cluen in range(len(cl)):
    print(str(cluen/len(cl)*100)+'%                ', end='\r')
    visited=[i for i in range(clues+sus)]
    visited.pop(cluen)
    shuffle(visited)
    while len(visited)>0:
        cl[cluen].append((visited.pop(-1), randint(-1000, 1000),randint(0, 1000),randint(0, 1000)))
    cl[cluen]=[len(cl[cluen])]+sorted(cl[cluen])

print("writing")

with open("opt.txt", "w") as f:
    f.write(str(clues)+' '+str(sus)+' 0\n')
    for cluen in range(len(cl)):
        f.write(str(cl[cluen]).replace(')','').replace('(','').replace(',',' ').replace('[','').replace(']','').replace('  ',' ')+'\n')



