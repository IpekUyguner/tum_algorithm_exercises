import collections
import sys

class Vertex:
    def __init__(self,key):
        self.id = key
        self.neighbors = {}

    def addNeighbor(self,neighbor):
        self.neighbors[neighbor] = 1

    def getNeighbors(self):
        return self.neighbors.keys()

    def getId(self):
        return self.id

class Graph:
    def __init__(self,N):
        self.vertList = {}
        for i in range(N):
            self.vertList[i] = Vertex(i)

    def addEdge(self,from_,to_):
        self.vertList[from_].addNeighbor(self.vertList[to_])
        self.vertList[to_].addNeighbor(self.vertList[from_]) #undirected graph

    def getVertex(self,n):
        return self.vertList[n]

def divide_groups(g,i,groups):
    groups[i] = 1
    queue = collections.deque([i])
    while queue:
        vertex = queue.popleft()
        g.getVertex(vertex)
        for neighbour in g.getVertex(vertex).getNeighbors():  #get the neighbors
            if(groups[neighbour.getId()] == -1):  # if not put into any group yet, put it to the other group
                queue.append(neighbour.getId())
                groups[neighbour.getId()] = 1- groups[vertex]   #adjust the group indexing
            else:
                if groups[neighbour.getId()] == groups[vertex]:   #if we encounter a contrast , the problem cannot be solved!
                    return False
    return True  #if we able to reach to the end, it means we can divide the topping into two without conflicts!

def is_doable(N):
    groups = [-1]*N
    for i in range(N):          #this part is for the disconnected subpart of the graph, our samples could be not strongly connected
        if groups[i] == -1:
            if divide_groups(g,i,groups) == False:
                return False
    return True

if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):
        info_line = list(map(int, sys.stdin.readline().split()))
        N =info_line[0]
        g= Graph(N)
        for i in range(info_line[1]):                            #create the graph
            vertices = list(map(int, sys.stdin.readline().split()))
            g.addEdge(vertices[0]-1,vertices[1]-1)        #indexing starts zero unlike the samples, so there is -1
        result = is_doable(N)
        if result:
            print('Case #{}: {}'.format(counter + 1, 'yes'))
        else:
            print('Case #{}: {}'.format(counter + 1, 'no'))
        if(counter != (int(total_case)-1)):
            sys.stdin.readline()








