import java.util.*;
import java.lang.*;
import java.util.PriorityQueue;


public class rescuemission
{
    public static class Edge implements Comparable<Edge>{
        int weight, start, end;

        public Edge(int weight, int start, int end) {
            this.weight = weight;
            this.start = start;
            this.end = end;
        }

        @Override
        public String toString() {
            return "dummy";
        }

        @Override
        public int compareTo(Edge o) {
            return this.weight - o.weight;
        }
    }

    public static void main (String[] args)
    {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        s.nextLine();

        for(int test = 0; test < t; test++)   // all cases
        {
            int number_rooms = s.nextInt();
            int number_connections = s.nextInt();
            int number_dungeons = s.nextInt();
            s.nextLine();
            int[][] graph = new int[number_rooms][number_rooms];

            List dungeon_list = new ArrayList();

            for(int j = 0; j < number_dungeons; j++)  //list of all dungeons
            {
                int dum = s.nextInt();
                dungeon_list.add(dum);
                s.nextLine();
            }

            for (int d = 0; d < number_rooms; d++)  // create the graph to calculate all shortest path between them.
            {
                for (int c = 0; c < number_rooms; c++)
                    graph[d][c] =  9999999;

                graph[d][d] = 0;
            }

            for(int j = 0; j < number_connections; j++)  // add the edges to the graph!
            {
                int source = s.nextInt();
                int end = s.nextInt();
                int weight = s.nextInt();
                s.nextLine();
                graph[source-1][end-1] =  Math.min(weight,graph[source-1][end-1]) ;
                graph[end-1][source-1] =  Math.min(weight, graph[end-1][source-1]);
            }

            for (int k = 0; k < number_rooms; k++)    //shortest paths for all pairs
            {
                for (int i = 0; i < number_rooms; i++)
                {
                    for (int j = 0; j < number_rooms; j++)
                    {
                        if (graph[i][k] + graph[k][j] < graph[i][j])
                            graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }


            PriorityQueue<Edge> minHeap = new PriorityQueue<>();
            ArrayList<ArrayList<Edge>> adjacencyList = new ArrayList<>();

            boolean[] visited = new boolean[number_dungeons];

            for(int j = 0; j < number_dungeons; j++)
            {                                                           //just dungeons graph.....
                visited[j] = false;
                adjacencyList.add(new ArrayList<>());
            }


            // we need to find the mst of  the dungeons. Here it is calculated by Prim algortihm.
            for (int first = 0; first < dungeon_list.size(); first++)
            {
                for (int second = 0; second < dungeon_list.size(); second++)
                {
                    if (first != second)
                        adjacencyList.get(first).add(new Edge( graph[(int) dungeon_list.get(first)-1][(int) dungeon_list.get(second)-1], first, second));
                }
            }

            for (int a= 0; a < adjacencyList.get(0).size(); a++)
                minHeap.add(adjacencyList.get(0).get(a));

            int cost = 0;

            if (!minHeap.isEmpty())
                visited[adjacencyList.get(0).get(0).start] = true;

            while (!minHeap.isEmpty())
            {
                Edge current_Edge = minHeap.remove();
                if(!visited[current_Edge.end])
                    cost += current_Edge.weight;

                visited[current_Edge.end] = true;
                for(Edge edge: adjacencyList.get(current_Edge.end))
                {
                    if(!visited[edge.end])
                        minHeap.add(edge);
                }
            }

            int min = 1000000;
            if( !dungeon_list.contains(0))    // add the first (beginning ) room , unless it is in the dungeon list. --> By connecting it to the nearest dungeon
            {
                for (int i = 0; i < dungeon_list.size(); i++)
                {
                    if (graph[0][(int)dungeon_list.get(i)-1] < min)
                        min = graph[0][(int)dungeon_list.get(i)-1];
                }
               cost  = cost +  min;
            }
            System.out.println("Case #" + (test+1) +  ": "+ cost);

            if (test != t-1 )
                s.nextLine();
        }
    }
}
