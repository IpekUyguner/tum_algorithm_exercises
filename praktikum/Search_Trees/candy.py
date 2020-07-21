from collections import defaultdict,deque
import sys
# After creating the graph, I add all the vertices with incoming edge size ==1 , until there is no mere vertix in the queue, pop the
#vertix from the queue and decrease its neighbors degree size by 1 and if that neighbor has degree size 1 , add it to the queue...
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_center(self,in_degree):
        q = deque()
        for i in range(self.V):
            if in_degree[i] == 1:
                q.append(i)

        keep_track = 0
        while q:  #until we finish all the nodes
            u = q.popleft()
            keep_track = u
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 1:      #if it is leaf node
                    q.append(i)
        return keep_track

if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):
        info_line = int(sys.stdin.readline())
        g = Graph(info_line)
        in_degree = [0] * (info_line)

        for i in range(info_line-1):  # create the graph
            new_edge = list(map(int, sys.stdin.readline().split()))
            g.addEdge(new_edge[0] , new_edge[1])
            in_degree[new_edge[1]]= in_degree[new_edge[1]]+1
            in_degree[new_edge[0]]= in_degree[new_edge[0]]+1

        result = g.find_center(in_degree)
        print('Case #{}: {}'.format(counter + 1, result))
        if(counter != (int(total_case)-1)):
            sys.stdin.readline()



