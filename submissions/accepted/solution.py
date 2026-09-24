#!/usr/bin/python3
import heapq as qq # drop in q with our own implementation later, if time permits.

# adjlist -> edgelist
def adjedge(adjlist)->list[[int, int, int], int, int]:
    edgelist=[]
    for i in adjlist:
        ...

def bellmanford(edgelist, src, count):
    dist=[None for _ in adjlist]
    prev=[None for _ in adjlist]    

    #Drop in implementation of qq as own module later if time permits
    q=[]
    qpush=lambda w, s, d:qq.heappush(q, (w, s, d))
    qpop=lambda:qq.heappop(q)

"""Parsing - vertices"""
def parse_adjlist():
    clues, suspects, freeclue=input().split()
    clues, suspects, freeclue=int(clues), int(suspects), int(freeclue)
    count=clues+suspects #Count for how many vertecies total
    cluesGraph=[]
    for i in range(clues): 
        # Get the number of total counts
        line=list(map(int, input().split()))[1:]
        cluesGraph.append([[line[4*j], line[4*j+1], line[4*j+2], line[4*j+3]] for j in range(0, (len(line))//4)])
    # treat suspects as a vertex with no outgoing, aka sink node type.
    for _ in range(suspects):cluesGraph.append([])
    return (cluesGraph, freeclue, clues, suspects)

"""Parsing - edges"""
def parse_edgelist():
    clues, suspects, freeclue=input().split()
    clues, suspects, freeclue=int(clues), int(suspects), int(freeclue)
    count=clues+suspects #Count for how many vertecies total
    cluesConnectionsList=[]
    for i in range(clues): 
        # Get the number of total counts
        line=list(map(int, input().split()))[1:]
        for j in range(0, len(line), 4):
            if line[j]<clues: #check if we are going to a suspect
                cluesConnectionsList.append((i, line[j], (line[j+1], line[j+2], line[j+3])))
                cluesConnectionsList.append((line[j], i, (line[j+1], line[j+2], line[j+3])))
            else: cluesConnectionsList.append((i, line[j], (line[j+1], line[j+2], line[j+3])))
    return (cluesConnectionsList, freeclue, clues, suspects)

tup=parse_edgelist()
print(tup)
order=bellmanford(tup[0], tup[1], tup[2]+tup[3])
