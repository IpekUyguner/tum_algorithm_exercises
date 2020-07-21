import sys
from collections import  defaultdict
from heapq import  heappush,heappop

def dijkstra(graph, source, N):
    q,distances = [],[]
    max = sys.float_info.max

    for i in range(N):
        if source != i:
            weight = max
        else:
            weight = 0
        distances.append(weight)

    heappush(q, [0, source])

    while q:
        w,v = heappop((q)) #(weight, vertix)
        for e in graph[v]:
            candidate_distance = distances[v] + e[1]
            if distances[e[0]] > candidate_distance:
                distances[e[0]] = candidate_distance
                heappush(q,[distances[e[0]], e[0]])
    return distances


if __name__ == "__main__":
    total_case = sys.stdin.readline()
    max = sys.float_info.max

    for c in range(int(total_case)):
        info_line = list(map(int, sys.stdin.readline().split()))
        g = defaultdict(list)
        markets = [50000] * info_line [0]
              #there will be one market per city with min time... 50000(random max number) means there isnt market in this city

        for i in range(info_line[1]): #for roads
            source,end,weight = list(map(int, sys.stdin.readline().split()))
            g[source-1].append((end-1, weight))
            g[end-1].append((source-1, weight))

        Lea_to_markets = dijkstra(g, info_line[3]-1, info_line[0])
        Peter_to_markets = dijkstra(g, info_line[4]-1, info_line[0])

        for i in range(info_line[2]): #for markets
            city, time = list(map(int, sys.stdin.readline().split()))
            markets[city-1] = min(time, markets[city-1])

        #finding all the markets which can be reachable from Lea and from Peter:
        results = [Lea_to_markets[i]+ Peter_to_markets[i] + markets[i] for i in range(len(markets))
                   if markets[i] != 50000 and Lea_to_markets[i] != max and Peter_to_markets[i] != max ]

        #finding the minimum distance amongs available markets:
        if len(results)> 0:
            result = min(results)  # in terms of minutes, change it .
            hours = result // 60
            minutes = result - hours * 60

            if(len(str(minutes)) == 1 ):
                minutes = "0" +str(minutes)
            print('Case #{}: {}'.format(c + 1, str(hours) + ":" + str(minutes)))
        else:
            print('Case #{}: {}'.format(c + 1,"impossible"))

        if(c != (int(total_case)-1)):
            sys.stdin.readline()




