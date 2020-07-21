import sys
from collections import deque,defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent,adjacency):
        visited = [False] * (self.ROW)

        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()
            neighbors = adjacency[u]
            filter_my = [i for i in (neighbors) if visited[i] == False and self.graph[u][i] > 0]
            for ind in (filter_my):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def FordFulkerson(self, source, sink, adjacency):
        parent = [-1] * (self.ROW)
        max_flow = 0
        max = sys.float_info.max

        while self.BFS(source, sink, parent,adjacency):
            path_flow = max
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

if __name__ == "__main__":
    total_case = sys.stdin.readline()
   # total_case = 1
    for c in range(int(total_case)):
        number_people, number_food, number_beverage = list(map(int, sys.stdin.readline().split()))
        g = [[0 for x in range(number_people+ number_food+ number_beverage+2)] for y in range(number_people+ number_food+ number_beverage+2)]

        adjacency = defaultdict(list)

        for i in range(number_people):
            food, drink = list(map(int, sys.stdin.readline().split()))
            g[0][food] = 1
            g[food][number_food+i+1] = 1
            g[number_food+i+1][number_food+number_people+drink] = 1
            g[number_food+number_people+drink][len(g[0])-1] = 1

            #adjacency list:
            adjacency[0].append(food)
            adjacency[food].append(0)

            adjacency[food].append(number_food+i+1)
            adjacency[number_food+i+1].append(food)

            adjacency[number_food+i+1].append(number_food+number_people+drink)
            adjacency[number_food+number_people+drink].append(number_food+i+1)

            adjacency[number_food+number_people+drink].append(len(g[0])-1)
            adjacency[len(g[0])-1].append(number_food+number_people+drink)





        gra = Graph(g)
        result = gra.FordFulkerson(0,len(g[0])-1,adjacency)
        print('Case #{}: {}'.format(c + 1, result))

        if (c != (int(total_case) - 1)):
            sys.stdin.readline()
