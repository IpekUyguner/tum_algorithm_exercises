import sys
class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        max = sys.float_info.max

        while self.BFS(source, sink, parent):
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

    for c in range(int(total_case)):
        number_vertices, number_edges = list(map(int, sys.stdin.readline().split()))
        source = 0
        sink = number_vertices-1
        #0 means there is no edge between these vertices.
        g = [[0 for x in range(number_vertices)] for y in range(number_vertices)]
        for i in range(number_edges):
            firstNode, secondNode, weight = list(map(int, sys.stdin.readline().split()))
            g[firstNode-1][secondNode-1] = weight + g[firstNode-1][secondNode-1]
            g[secondNode-1][firstNode-1] = weight + g[secondNode-1][firstNode-1]

        graph = Graph(g)
        flow = graph.FordFulkerson(0,number_vertices-1)
        if flow == 0:
            print('Case #{}: {}'.format(c + 1,"impossible"))
        else:
            print('Case #{}: {}'.format(c + 1,flow))



        if (c != (int(total_case) - 1)):
            sys.stdin.readline()

