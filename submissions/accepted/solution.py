#!/usr/bin/python3
import heapq as qq # drop in q with our own implementation later, if time permits.

def bellmanford(edgelist, src, count, weight_key=lambda w, visited=False:w[1]+w[2]if visited and w[0]<0 else sum(w)):
    
    Infinity=None
    dist=[Infinity for _ in adjlist] 
    prev=[None for _ in adjlist]

    # check if src of any connection is visited (visited src -> no more bribe)
    # Therefore, only set to true after visiting every child once
    visited=[False for _ in adjlist] 

    dist[src]=0

    #Drop in implementation of qq as own module later if time permits
    q=[]
    qpush=lambda w, s, d:qq.heappush(q, (w, s, d))
    qpop=lambda:qq.heappop(q)

    for _ in range(count-1): #count-1 relaxations
        # check every connection!
        for s, d, w in edgelist:
            if dist[s]==Infinity: continue # Skip if the src of the connection is not connected to src of traversal
            else: if dist[d]==Infinity or dist[d]+weight_key(visited=)

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
    return (cluesConnectionsList, freeclue, clues, suspects)

tup=parse_edgelist()
print(tup)
order=bellmanford(tup[0], tup[1], tup[2]+tup[3])
