import java.time.LocalTime;
import java.util.*;

public class alarm
{
     public static boolean check(List<Integer> current_time, int n, List<List<Integer>> input_list,HashMap<Integer, List<Integer>> possible_numbers,HashMap<Integer, List<Integer>> no_sticks, HashMap<Integer, HashSet<Integer>> functioning_Sticks,HashMap<Integer, List<Integer>> sticks)
    {
        // Check if it is possible to reach this representation
        if ((!possible_numbers.get(input_list.get(n).get(0)).contains(Integer.valueOf(current_time.get(0)))) ||
                (!possible_numbers.get(input_list.get(n).get(1)).contains(Integer.valueOf(current_time.get(1)))) ||
                (!possible_numbers.get(input_list.get(n).get(2)).contains(Integer.valueOf(current_time.get(2)))) ||
                (!possible_numbers.get(input_list.get(n).get(3)).contains(Integer.valueOf(current_time.get(3)))))
            return false;


        // Check if we can represent this current time by more segment, if so there is sth inconssistent . output no:
        for(Integer x : sticks.get(Integer.valueOf(current_time.get(0)))) // get all bars of the 0th digit and
            //check if it is in the functioning bar lists but clock didnt use it ->> not valid
            if (functioning_Sticks.get(0).contains(x) && no_sticks.get(input_list.get(n).get(0)).contains(x))
                return false;

        for(Integer x : sticks.get(Integer.valueOf(current_time.get(1))))
            if (functioning_Sticks.get(1).contains(x) && no_sticks.get(input_list.get(n).get(1)).contains(x))
                return false;

        for(Integer x : sticks.get(Integer.valueOf(current_time.get(2))))
            if (functioning_Sticks.get(2).contains(x) && no_sticks.get(input_list.get(n).get(2)).contains(x))
                return false;

        for(Integer x : sticks.get(Integer.valueOf(current_time.get(3))))
            if (functioning_Sticks.get(3).contains(x) && no_sticks.get(input_list.get(n).get(3)).contains(x))
                return false;
        return true;
    }

    public static void main(String[] args)
    {

        //HERE IS THE ALL POSSIBLE DIGITS FROM EACH DIGITS.
        //FOR EXAMPLE-> observed 0 can be 0 or 8 in reality.
        HashMap<Integer, List<Integer>> possible_numbers = new HashMap<>();
        List<Integer> d0 = Arrays.asList(0,8);
        possible_numbers.put(0,d0);
        List<Integer> d1 = Arrays.asList(0,1,3,4,7,8,9);
        possible_numbers.put(1,d1);
        List<Integer> d2 = Arrays.asList(2,8);
        possible_numbers.put(2,d2);
        List<Integer> d3 = Arrays.asList(3,8,9);
        possible_numbers.put(3,d3);
        List<Integer> d4 = Arrays.asList(4,8,9);
        possible_numbers.put(4,d4);
        List<Integer> d5 = Arrays.asList(5,6,8,9);
        possible_numbers.put(5,d5);
        List<Integer> d6 = Arrays.asList(6,8);
        possible_numbers.put(6,d6);
        List<Integer> d7 = Arrays.asList(0,3,7,8,9);
        possible_numbers.put(7,d7);
        List<Integer> d8 = Arrays.asList(8);
        possible_numbers.put(8,d8);
        List<Integer> d9 = Arrays.asList(8,9);
        possible_numbers.put(9,d9);


        //HERE IS THE STICKS WHICH ARE SWITCHED ON FOR EACH DIGITS:
        //STICKS ARE NUMBERED AS BELOW.
        HashMap<Integer, List<Integer>> sticks = new HashMap<>();
        d0 = Arrays.asList(1,2,3,4,5,6);
        sticks.put(0,d0);
        d1 = Arrays.asList(3,4);
        sticks.put(1,d1);
        d2 = Arrays.asList(2,3,7,6,5);
        sticks.put(2,d2);
        d3 = Arrays.asList(2,3,4,5,7);
        sticks.put(3,d3);
        d4 = Arrays.asList(1,7,3,4);
        sticks.put(4,d4);
        d5 = Arrays.asList(1,2,7,4,5);
        sticks.put(5,d5);
        d6 = Arrays.asList(1,2,4,5,7,6);
        sticks.put(6,d6);
        d7 = Arrays.asList(2,3,4);
        sticks.put(7,d7);
        d8 = Arrays.asList(1,2,3,4,5,6,7);
        sticks.put(8,d8);
        d9 = Arrays.asList(1,2,3,4,5,7);
        sticks.put(9,d9);
        //     2
        //   --------                               <----- each stick mapping like this.
        // 1 |       | 3
        ///  |---7---|
        // 6 |       | 4
        //   |-------|
       //        5


        // HERE IS THE STICKS NUMBERS WHICH ARE SWITCHED OFF FOR EACH DIGIT.
        HashMap<Integer, List<Integer>> no_sticks = new HashMap<>();
        d0 = Arrays.asList(7);
        no_sticks.put(0,d0);
        d1 = Arrays.asList(1,2,5,6,7);
        no_sticks.put(1,d1);
        d2 = Arrays.asList(1,4);
        no_sticks.put(2,d2);
        d3 = Arrays.asList(1,6);
        no_sticks.put(3,d3);
        d4 = Arrays.asList(2,5,6);
        no_sticks.put(4,d4);
        d5 = Arrays.asList(3,6);
        no_sticks.put(5,d5);
        d6 = Arrays.asList(3);
        no_sticks.put(6,d6);
        d7 = Arrays.asList(1,6,7,5);
        no_sticks.put(7,d7);
        d8 = Arrays.asList(0);
        no_sticks.put(8,d8);
        d9 = Arrays.asList(6);
        no_sticks.put(9,d9);

        Scanner s = new Scanner(System.in);
        int tests = s.nextInt();
        s.nextLine();
        for(int x=0; x<tests; x++)
        {
                List<String> results = new ArrayList<>();
                HashMap<Integer, HashSet<Integer>> functioning_Sticks = new HashMap<>();;
                for (int i=0; i<4; i++)
                    functioning_Sticks.put(i, new HashSet<>());

                int count = s.nextInt();
                s.nextLine();
                List<List<Integer>> input_list = new ArrayList<>();
                for(int a=0; a<count;a++)
                    input_list.add(new ArrayList<>());

                for(int i=0; i<count;i++)
                {
                    String str = s.nextLine();
                    String[] list = str.split(""); //keep the observed time inputs in array.
                    input_list.get(i).add(Integer.valueOf(list[0]));
                    input_list.get(i).add(Integer.valueOf(list[1]));
                    input_list.get(i).add(Integer.valueOf(list[3]));
                    input_list.get(i).add(Integer.valueOf(list[4]));

                    functioning_Sticks.get(0).addAll(sticks.get(Integer.valueOf(list[0]))); //keep all the functioning bars for each digits
                    functioning_Sticks.get(1).addAll(sticks.get(Integer.valueOf(list[1])));
                    functioning_Sticks.get(2).addAll(sticks.get(Integer.valueOf(list[3])));
                    functioning_Sticks.get(3).addAll(sticks.get(Integer.valueOf(list[4])));
                }


            List<List<Integer>> possible_starts = new ArrayList<>();
            for (int index1 : possible_numbers.get(Integer.valueOf(input_list.get(0).get(0))))
                for (int index2 : possible_numbers.get(Integer.valueOf(input_list.get(0).get(1))))
                    for (int index3 : possible_numbers.get(Integer.valueOf(input_list.get(0).get(2))))
                        for (int index4 : possible_numbers.get(Integer.valueOf(input_list.get(0).get(3))))
                            if (((index1<=1 && index2<=9) || (index1==2 && index2<=3)) && (index3<=5 && index4<=9)) //normal hour style
                                possible_starts.add(Arrays.asList(index1,index2,index3,index4));


            for (List<Integer> candidate : possible_starts) // for each possible start, check if the rest of the input time con
                //sistent. If so, add to the result list.
            {
                List<Integer> temporary = candidate; // assume this starting point is true, check every other later
                /// minutes can be possibly represented by observed time
                boolean che= false;
                for (int i=0; i<count; i++)
                {
                    if (!check(temporary,i,input_list,possible_numbers,no_sticks,functioning_Sticks,sticks))
                    {
                        che=true;
                        break;
                    }
                    String dummy ="";
                    for(int y=0; y<temporary.size();y++)
                        dummy = dummy + String.valueOf(temporary.get(y));

                    dummy = dummy.substring(0,2) + ":" + dummy.substring(2,4);
                    LocalTime lt = LocalTime.parse(dummy);
                    lt = lt.plusMinutes(1);  // get the next minute and compare its observed representation
                    String[] ssss = String.valueOf(lt).split("");
                    //TO DO: change this part.
                    temporary = new LinkedList<>();
                    for(int a=0;a<ssss.length;a++)  // just dummy part to convert data types each other.
                    {
                       if(!ssss[a].equals(":"))
                           temporary.add(Integer.valueOf(ssss[a]));
                    }
                }
                String d= "";
                for(int y=0;y<4;y++)
                    d+=candidate.get(y);
                d = d.substring(0,2) + ":" + d.substring(2,4);

                if(!che)
                    results.add(d);
            }
            System.out.println("Case #" + (x+1) + ": ");

            if(results.size()!=0)
                for (int z = 0; z < results.size(); z++)
                    System.out.println(results.get(z));
            else
                System.out.println("none");

            if(x!= tests-1)
                s.nextLine();
        }
    }
}
