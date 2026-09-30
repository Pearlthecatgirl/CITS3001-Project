#!/usr/bin/python3

maxpossible=float("inf")

def dijkstra(adjlist, src, count):
    import heapq as qq
    Infinity=maxpossible
    dist, prev=[Infinity for _ in range(count)], [None for _ in range(count)]

    q=[]
    qpush=lambda x:qq.heappush(q, x)
    qpop=lambda:qq.heappop(q)

    qpush((None, src, 0))
    while (len(q)>0):
        s, d, w=qpop()
        if dist[d] is not Infinity: continue #visited before
        dist[d]=w
        prev[d]=s
        for v, wf, wm, wp in adjlist[d]:
            wtotal=wf+wm+wp
            if dist[v] is not Infinity: continue
            qpush((d, v, wtotal+w))
    return dist, prev

def permutation(edgelist, src, clues, sus):
    weight_function=lambda w, visited=False:w[1]+w[2]if visited and w[0]<0 else sum(w)
    Infinity=maxpossible
    count=clues+sus
    from collections import deque
    paths = []
    nextnode = deque()

    # Start with a path containing the src
    nextnode.append(([src], src))

    while nextnode:
        path,node=nextnode.popleft()
        for edge in edgelist:
            if edge[0] == node:
                new_path = path + [edge]
                if len(new_path)<=count:
                    paths.append(new_path)
                    nextnode.append((new_path, edge[1]))
    
    p2=[]
    for i in paths:
        if i[-1][1]>=clues: 
            p2.append(i) #remove all crossroad paths, aka paths that dont fully reach the end
    
    suscount=[Infinity for _ in range(sus)]
    for p in p2:
        visited=[False for _ in edgelist]
        w=0
        for node in p[1:]:
            n=edgelist.index(node)
            w+=weight_function(node[-1], visited[n])
            visited[n]=False
        if w<suscount[p[-1][1]-clues]:
            suscount[p[-1][1]-clues]=w
    #print(suscount)
    return suscount

def bellmanford(edgelist, src, count, weight_key=lambda w, visited=False:w[1]+w[2]if visited and w[0]<0 else sum(w)):
    Infinity=maxpossible
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
        line=list(map(int, input().split()))
        # Get the number of total counts line=list(map(int, input().split()))[1:]
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

def mysort(array, key):
    return sorted(array, key=key)

def output(distances, clues, suspects):
    total_effort=lambda s:distances[clues+s] #O(1)
    order=[i for i in range(suspects)]
    return mysort(order, key=total_effort)

def accepted_answer():
    tup=parse_edgelist()
    order=bellmanford(tup[0], tup[1], tup[2]+tup[3])
    opt=output(order[0], tup[2], tup[3])
    s=""
    for i in opt: s+=str(i)+' '
    print(s)

def wrong_answer():
    tup=parse_adjlist()
    order=dijkstra(tup[0], tup[1], tup[2]+tup[3])
    opt=output(order[0], tup[2], tup[3])
    s=""
    for i in opt: s+=str(i)+' '
    print(s)

def timeout_answer():
    tup=parse_edgelist()
    order=permutation(tup[0], tup[1], tup[2], tup[3])
    opt=output([[] for _ in range(tup[2])]+order, tup[2], tup[3])
    s=""
    for i in opt: s+=str(i)+' '
    print(s)

wrong_answer()
