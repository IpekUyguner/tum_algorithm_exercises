from collections import defaultdict,deque
import sys
#IPEK UYGUNER


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # for finding the longest distance between first and last node == scheduling problem!
    def topologicalSort(self, coming_Edges,weights):
        q = deque()
        dist = weights
        in_degree = [0] * (V)

        for i in range(self.V):
            in_degree[i] = len(keep_coming_edges[i])
            if len(keep_coming_edges[i]) == 0:
                q.append(i)
        check = False

        while q:
            u = q.popleft()
            max = -10
            for i in coming_Edges[u]:
                if dist[i] + weights[u] > max:
                    max = dist[i] + weights[u]
                    check = True
            if check:
                dist[u] = max

            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
        return dist[V-1]

if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):
        V = int(sys.stdin.readline())
        g = Graph(V)

        keep_coming_edges = defaultdict(list)
        weights = defaultdict(list)

        for i in range(V):  # create the graph
            new_edges = list(map(int, sys.stdin.readline().split()))
            [(g.addEdge(i,dest-1), keep_coming_edges[dest-1].append(i))  for dest in new_edges[2:]]
            weights[i] = new_edges[0]

        result = g.topologicalSort(keep_coming_edges,weights)
        print('Case #{}: {}'.format(counter + 1, result))

        if(counter != (int(total_case)-1)):
            sys.stdin.readline()
