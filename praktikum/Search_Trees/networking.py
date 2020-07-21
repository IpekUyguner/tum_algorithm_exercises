import sys
parent = dict()
rank = dict()
#This is a simple example of creating MST.  The edges in the tree must be small as much as possible. Create MST by Kruskal
def find(v):
    p = parent[v]
    while p != parent[p]:
        q = parent[p]
        parent[p] = parent[q]
        p = q
    return p

def union(v1, v2):   #like last week: union algortihm
    vertix_1 = find(v1)
    vertix_2 = find(v2)
    if vertix_1 != vertix_2:
        if rank[vertix_1] > rank[vertix_2]:
            parent[vertix_2] = vertix_1
        else:
            parent[vertix_1] = vertix_2
    if rank[vertix_1] == rank[vertix_2]:
        rank[vertix_2] = 1 +rank[vertix_2]

def kruskal_algorithm(vertices,edges):
    minimum_spanning_tree = set()
    for vertix in range(vertices):
        parent[vertix] = vertix
        rank[vertix] = 0

    for edge in edges:
        weight, vertice1, vertice2 = list(map(int,edge))
        if find(vertice1) != find(vertice2):  #prevents loops as well...
            union(vertice1, vertice2)
            result = (vertice1+1,vertice2+1)
            minimum_spanning_tree.add(result)
    return sorted(minimum_spanning_tree)

if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):
        N = int(sys.stdin.readline())
        edges = []

        for i in range(N):  #create the graph
            current_line = list(map(int, sys.stdin.readline().split()))
            for j in range(i,N):
                if i !=j :
                    result = (current_line[j],i,j)
                    edges.append(result)
        edges.sort(key=lambda x: x[0])  # To sort by first element of the tuple
        tree_Resulted = kruskal_algorithm(N,edges)
        print('Case #'+ str(counter+1)+ ":")
        for i in range(len(tree_Resulted)):
            print(*tree_Resulted[i])
        if(counter != (int(total_case)-1)):
            sys.stdin.readline()











