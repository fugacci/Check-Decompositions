def menu0():
    return raw_input('Enter name of file in input: ')

from sets import Set


from itertools import chain, combinations

import time

def powerset_generator(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        yield Set(subset)

def intersection(X,Y):
    I=Set([])
    for p in X:
        for q in Y:
            if len(p & q)>1:
                I.add(p & q)
    return I


class graph:

    def __init__(self):
        self.neighbors = {}

    def add_vertex(self, v):
        if v not in self.neighbors:
            self.neighbors[v] = []

    def add_edge(self, u, v):
        self.neighbors[u].append(v)
        # if u == v, do not connect u to itself twice
        if u != v:
            self.neighbors[v].append(u)

    def vertices(self):
        return list(self.neighbors.keys())

    def vertex_neighbors(self, v):
        return self.neighbors[v]

def is_cyclic_graph(G):

    Q = []
    V = G.vertices()

    # initially all vertices are unexplored
    layer = { v: -1 for v in V }

    for v in V:

        # v has already been explored; move on
        if layer[v] != -1:
            continue

        # take v as a starting vertex
        layer[v] = 0
        Q.append(v)

        # as long as Q is not empty
        while len(Q) > 0:

            # get the next vertex u of Q that must be looked at
            u = Q.pop(0)

            C = G.vertex_neighbors(u)

            for z in C:
                # if z is being found for the first time
                if layer[z] == -1:
                    layer[z] = layer[u] + 1
                    Q.append(z)
                elif layer[z] >= layer[u]:
                    return True

    return False

#graph class and is_cyclic_graph(G) are due to http://diego.assencio.com/?index=e83a797bcee562e2f1a4faa9293316ab

def hasCycle(Z,N):
    GG=graph()
    for i in range(1, N+1):
        GG.add_vertex(i)
    for z in Z:
        Listz=[]
        for w in z:
            Listz=Listz+[w]
        GG.add_edge(Listz[0], Listz[1])
    if is_cyclic_graph(GG):
        return 1
    else :
        return 0

L= Set([])

nome=menu0()
start_time = time.time()
file=open(nome, 'r+')
l=1
Nt=0
for line in file:
    if l==1:
        Nv=int(line)
        l+=1
    else:
        a, b, c = [int(i) for i in line.split()]
        L.add(Set([a,b,c]))
        Nt+= 1

file.close()

print "Number of vertices is %s" %Nv
print "Number of top simplices is %s" %Nt
#print "The top simplices are %s" %L


check=0
number=0

for x in powerset_generator(L):
    if len(x)>0 and len(x)<=len(L)/2:
        if hasCycle(intersection(x,L-x), Nv)==1:
            check+= 1
            #print "First Component"
            #print x
            #print "Second Component"
            #print L-x
            #print "Intersection"
            #print intersection(x,L-x)
            #print "Above Intersection has non-null 1-homology"
        #else:
            #print "First Component"
            #print x
            #print "Second Component"
            #print L-x
            #print "Intersection"
            #print intersection(x,L-x)
            #print "Above Intersection has null 1-homology"
        number+=1
        #if number%1000000==0:
        #    print "Analyzed decompositions: %s millions" %(number/1000000)
        #    print "Required time to reach this point: %s seconds" %(round(time.time() - start_time, 2))

if check==0:
    print "Each decomposition has intersection with null 1-homology"
elif check==number:
    print "Each decomposition has intersection with non-null 1-homology"
else :
    print "There exist both decompositions having intersection with null 1-homology and decompositions having intersection with non-null 1-homology"

#print "Number of checked decompositions: %s" %number
#print "Number of decompositions having intersection with non-null 1-homology: %s" %check

print "Required time: %s seconds" %(round(time.time() - start_time, 2))
