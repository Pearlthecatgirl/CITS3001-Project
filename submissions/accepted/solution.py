#!/usr/bin/python3

def bellmanford(edgelist, src, count, weight_key=lambda w, visited=False:w[1]+w[2]if visited and w[0]<0 else sum(w)):
    Infinity=None
    dist, prev=[Infinity for _ in range(count)], [None for _ in range(count)]
    # if nth edge is visited, do not give the bribe.
    visited=[False for _ in edgelist] 

    dist[src]=0

    # O((count-1)*|E|)=O((|V|-|suspects|)*|E|)=O(VE)
    for _ in range(count-1): #count-1 relaxations
        # check every connection!
        for n in range(len(edgelist)): # at worst case, every edge is connected, so touch every edge
            s, d, w=edgelist[n]
            if dist[s]==Infinity: continue # Skip if the src of the connection is not connected to src of traversal
            else: 
                # relaxation by checking if currently disconnected, or the src+w(src,dest)<w(dest)
                # visited[n] is checked to see if bribe applies
                if dist[d]==Infinity or dist[s]+weight_key(w, visited=visited[n])<dist[d]:
                    dist[d]=dist[s]+weight_key(w, visited=visited[n]) #weight_key ->O(1)
                    prev[d]=s
                    visited[n]=True # this connection has been made, no more bribes are given
    return (dist, prev)

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
    for i in range(clues):  #(O(|E|), touches each edge once
        # Get the number of total counts
        line=list(map(int, input().split()))[1:]
        for j in range(0, len(line), 4):
            cluesConnectionsList.append((i, line[j], (line[j+1], line[j+2], line[j+3])))
    return (cluesConnectionsList, freeclue, clues, suspects)

# Add implementation here
def mysort(array, key):
    return sorted(array, key=key)

def output(distances, clues, suspects):
    total_effort=lambda s:distances[clues+s] #O(1)
    order=[i for i in range(suspects)]
    return mysort(order, key=total_effort)

tup=parse_edgelist()
order=bellmanford(tup[0], tup[1], tup[2]+tup[3])
print(output(order[0], tup[2], tup[3]))
