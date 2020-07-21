from collections import defaultdict
import sys
#In this code, I do toposort on directed roads, if it is acylic, then we have chance to add new roads by preserving the acylic feature
#But if the directed roads have already cycle, we cannot make it acylic by just adding new roads(edges).So if it is cyclic at the beginning
# just print impossible, otherwise we can add new directional edges from the smaller valued nodes towards to bigger valued nodes-This will
#preserve the acylic property...
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        in_degree = [0] * (self.V)
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0                  #visited vertices count
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            count += 1

        if count != self.V:
            return top_order,"no"
        else:
            return top_order,"yes"

if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):
        info_line = list(map(int, sys.stdin.readline().split()))
        g = Graph(info_line[0])
        #edgeeee =[[0,1],[3,2]]
        if(int(info_line[0]) == 1): #just special case
            print('Case #{}: {}'.format(counter + 1, 'yes'))
        else:
            for i in range(info_line[1]):                            #create the graph
                new_edge = list(map(int, sys.stdin.readline().split()))
                g.addEdge(new_edge[0]-1,new_edge[1]-1)
            topo_list, acaylyc = g.topologicalSort()

            if acaylyc == 'no':    #if cylic nothing to do.....
                for i in range(info_line[2]):
                    dummy = sys.stdin.readline()
                print('Case #{}: {}'.format(counter + 1, 'no'))

            else: #not cyclc, add edges from smaller valued node to the bigger valued in toposort
                show_result =[]
                for i in range(info_line[2]):
                    undirected_edge = list(map(int, sys.stdin.readline().split()))
                    if(topo_list.index(undirected_edge[0]-1) < topo_list.index(undirected_edge[1]-1)):
                        dummy = (undirected_edge[0], undirected_edge[1])
                        show_result.append(dummy)
                    else:
                        dummy = (undirected_edge[1], undirected_edge[0])
                        show_result.append(dummy)
                print('Case #{}: {}'.format(counter + 1, 'yes'))
                for i in range(len(show_result)):
                    print(*show_result[i])

        if(counter != (int(total_case)-1)):
            sys.stdin.readline()







