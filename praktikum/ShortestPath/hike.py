import sys
from collections import  defaultdict
from heapq import  heappush,heappop

#IPEK UYGUNER
#This code calculates the shortest distance between given two node,i.e.,1st and n-th node by Dijistkra algorithm.

def dijkstra(graph, source, end, N):
    q,distances = [],[]
    for i in range(N):
        if source == i:
            weight = 0
        else:
            weight = float("inf")
        distances.append(weight)

    heappush(q, [0, source])

    while q:
        w,v = heappop((q)) #(weight, vertix)
        for e in graph[v]:
            candidate_distance = distances[v] + e[1]
            if distances[e[0]] > candidate_distance:
                distances[e[0]] = candidate_distance
                heappush(q,[distances[e[0]], e[0]])
    return distances[end]


if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for c in range(int(total_case)):
        info_line = list(map(int, sys.stdin.readline().split()))
        g = defaultdict(list)
        for i in range(info_line[1]):      #creates the undirectional net.
            new_edge = list(map(int, sys.stdin.readline().split()))
            g[new_edge[0]-1].append((new_edge[1]-1, new_edge[2]))
            g[new_edge[1]-1].append((new_edge[0]-1, new_edge[2]))

        result = dijkstra(g, 0, info_line[0]-1, info_line[0])
        print('Case #{}: {}'.format(c + 1,result))
        if(c != (int(total_case)-1)):
            sys.stdin.readline()




