import java.util.*;
import java.util.Scanner;

public class football
{
    static int visitedToken = 1;

    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int first,second;
        int test = s.nextInt();
        s.nextLine();

        for (int xxx = 0; xxx < test ; xxx++)
        {
            int numTeams= s.nextInt();
            int numMatch = s.nextInt();
            s.nextLine();
            int[] wins = new int[numTeams];
            int[][] against = new int [numTeams][numTeams];
            Map<Integer, List<Integer>> map = new HashMap<>();
            String[] results = new String[numTeams];
            int[] total_remaning = new int[numTeams];

            for (int a = 0; a < numTeams; a++)
                for(int b = 0; b < numTeams; b++)
                    against[a][b] = 0;

            for (int j = 0; j < numTeams ; j++){
                wins[j] = s.nextInt();
                total_remaning[j] = 0;
            }

            s.nextLine();


            for (int j = 0; j < numMatch ; j++)
            {
                first = s.nextInt();
                second = s.nextInt();
                against[first-1][second-1] +=1;
                against[second-1][first-1] +=1;

                total_remaning[first-1]  +=1;
                total_remaning[second-1] +=1;
                s.nextLine();
            }

            int index = 0;
            for (int a = 0; a < numTeams; a++)
            {
                for (int b = a+1; b < numTeams; b++)
                {
                    if(against[a][b] > 0)
                    {
                        List<Integer> list = new ArrayList<Integer>();
                        list.add(a+1);
                        list.add(b+1);
                        map.put(index,list);
                        index +=1;
                    }
                }
            }


            for (int a = 0; a < numTeams; a++)
            {
                for (int b = 0; b < numTeams; b++)
                {
                    if(a != b &&  wins[a] + total_remaning[a] < wins[b])
                        results[a] = "no";
                }
            }

            for(int team = 0 ; team < numTeams; team++)
            {
                if( results[team]== null )
                {
                    int currentNode = team + 1;
                    visitedToken = 1;
                    int sumtotal = 0;
                    int[][] graph = new int [numTeams+2+index][numTeams+2+index];

                    for (int e= 0; e <numTeams+2+index; e++)
                        for(int m= 0 ; m <numTeams+2+index; m++)
                            graph[e][m] = 0;

                    for (int i= 0 ; i < index; i++)
                    {
                        if(currentNode != map.get(i).get(0) && currentNode!= map.get(i).get(1))
                        {
                            graph[0][i+1] = against[map.get(i).get(0)-1][map.get(i).get(1)-1];
                            graph[i+1][index +map.get(i).get(0)] = Integer.MAX_VALUE;
                            graph[i+1][index +map.get(i).get(1)] = Integer.MAX_VALUE;
                            sumtotal += against[map.get(i).get(0)-1][map.get(i).get(1)-1];
                        }

                    }
                    for (int i= 0 ; i<numTeams; i++)
                    {
                        if(currentNode -1 != i)
                            graph[index+i+1][index + numTeams+1] = wins[currentNode-1] - wins[i] + total_remaning[currentNode-1];
                    }
                    int maxFlow = fordFulkerson(graph,0, index+ numTeams+1);
                    if(maxFlow == sumtotal)
                        results[team] ="yes";
                    else
                        results[team] ="no";

                }

            }

            String txt = "";
            for (int a = 0 ; a < results.length; a++)
                txt = txt + " "+ results[a] ;
            System.out.println("Case #" + (xxx+1) + ":" + txt);

        }


    }

    public static int fordFulkerson(int[][] caps, int source, int sink)
    {
        int n = caps.length;
        int [] visited = new int[n];

        for(int maxFlow = 0;;)
        {
            int flow = dfs(caps, visited, source, sink, Integer.MAX_VALUE);
            visitedToken++;
            maxFlow += flow;
            if (flow == 0)
            {
                return maxFlow;
            }
        }
    }
    private static int dfs(int[][] caps, int[] visited, int node, int sink, int flow)
    {
        if (node == sink) return flow;
        int[] cap = caps[node];
        visited[node] = visitedToken;

        for (int i = 0; i < cap.length; i++) {
            if (visited[i] != visitedToken && cap[i] > 0)
            {

                if (cap[i] < flow) flow = cap[i];
                int dfsFlow = dfs(caps, visited, i, sink, flow);

                if (dfsFlow > 0)
                {
                    caps[node][i] -= dfsFlow;
                    caps[i][node] += dfsFlow;
                    return dfsFlow;
                }
            }
        }return 0;
    }


}


