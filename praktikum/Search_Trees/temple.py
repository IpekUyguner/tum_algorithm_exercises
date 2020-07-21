import sys
from collections import defaultdict
import heapq
#In this code, the aim is to create the MST of the rooms, I start with the room 1 and extend the tree by adding biggest edges which
#is from the visited rooms list(by using priorty queue) but if we can't add new edges, try to find some control rooms which already visited
#to draw the water level and continue to span the tree.
if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):
        info_line = list(map(int, sys.stdin.readline().split()))
        number_rooms = info_line[0]
        number_halls = info_line[1]
        number_controls = info_line[2]
        initial_water = info_line[3]
        g = defaultdict(list)

        if number_rooms ==1:
            print('Case #{}: {}'.format(counter + 1, info_line[3]))

        for i in range(number_halls):  # create the graph
            new_edge = list(map(int, sys.stdin.readline().split()))
            g[new_edge[0]].append((-new_edge[2], -new_edge[1]))
            g[new_edge[1]].append((-new_edge[2], -new_edge[0]))

        control_room = defaultdict(int)
        for i in range(number_controls):  # create the control rooms info array
            room_drain = list(map(int, sys.stdin.readline().split()))
            control_room[room_drain[0]] = room_drain[1]

        if number_rooms !=1:
            connected = set([])
            pq = []
            found = False
            connected.add(1)
            check = 1
            for tup in g[1]:   #Start point is node 1 . Add the all edges from node 1 to the queue
                heapq.heappush(pq, tup)
            while pq: # until there is an element in the queue
                w,b = list(i * -1 for i in heapq.heappop(pq)) #to get the max (heappop gives min), i just multiple everthing with -1,
                if w < initial_water and b not in connected:  #current hallway water level does not let us go further, so we need to
                    # draw the water:check if there is a visited room which can draw the water till this level.
                    a = {k: v for k, v in control_room.items() if v <= w and k in connected} ## a is the list of rooms which can draw the water to w
                    if a:
                        initial_water = w # draw to water till w (not more than w )
                        connected.add(b) # continue to adding edge b
                        check += 1
                        for tup in g[b]:
                            heapq.heappush(pq, tup)
                    else:
                        break

                elif b not in connected and w >= initial_water: #if current edge(hallway water level) is smaller than temple water level, we can
                    #continue to extend minimum spanning tree if only b is not already added to the mst.
                    connected.add(b)
                    check +=1
                    for tup in g[b]:
                        heapq.heappush(pq, tup)
                if check == number_rooms: # at the end if we able to visit all the rooms, the count will be our total room number
                    found = True
                    break

            if found == False:
                print('Case #{}: {}'.format(counter + 1, "impossible"))
            else:
                print('Case #{}: {}'.format(counter + 1, initial_water))
        if(counter != (int(total_case)-1)):
            sys.stdin.readline()
