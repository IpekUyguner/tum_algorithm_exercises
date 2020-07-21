import java.text.DecimalFormat;
import java.util.Scanner;

public class draw_lots {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String t = s.nextLine();
        for (int a = 1; a <= Integer.parseInt(t); a++)  // for each test cases:
        {
            String[] info = s.nextLine().split(" ");   //number of prizes and cost values taken here.
            String[] prizes_list = s.nextLine().split(" ");

            double high = 1.0, low = 0.0, payoff= 0, prob=0.0, e= 0.000000001;
            while(low  + e < high)              //we want actually the max probabilitx while the payoff is negative
            {
                prob = (low + high)/2.0;
                payoff = total_lost_with_prob_p(prob, prizes_list)-Double.parseDouble(info[1]);
                if(payoff <=0)                        //we can still increase the probability, so increase the low
                    low = prob;
                else            // we have positive payoff,make the prob little smaller so that we can have smaller payoff
                    high = prob;
            }
            DecimalFormat formatter = new DecimalFormat("#0.0000000000");
            System.out.println("Case #" + a + ": " + formatter.format(prob));
            if(a!= Integer.parseInt(t))   //Get rid of the empty lines.
                s.nextLine();

        }
    }

    static double total_lost_with_prob_p(double p, String[] prizes_list)  //function for calculating payoff
    {
        Double result = 0.0;
        for(int i = 0; i<= prizes_list.length-1; i++)
            result += Double.parseDouble(prizes_list[i])* Math.pow(p,i+1);
        return result;
    }
}
