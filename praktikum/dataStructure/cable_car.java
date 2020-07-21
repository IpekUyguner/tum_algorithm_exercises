import java.util.*;
import java.lang.*;
import java.text.DecimalFormat;

//I use the code from the link: https://stackoverflow.com/questions/43891998/place-n-points-while-maximizing-the-minimum-distance

class cable_car
{
    public static void main (String[] args)
    {
        Scanner s = new Scanner (System . in );
        String t = s.nextLine();
        for (int a= 1; a<= Integer.parseInt(t); a++)
        {
            String[] current_line = s.nextLine().split(" ");
            find_maxmin_distance(Double.parseDouble(current_line[0]),Integer.parseInt(current_line[1]),
                                 Double.parseDouble( current_line[2]), Double.parseDouble(current_line[3]), a);
        }
    }

    static void find_maxmin_distance(double d, int n, double s, double e, int a)
    {
        double high = d, low = 0;
        while(low + 0.0001 < high)
        {
            double gap_size = (low + high)/2;
            int gapsOnLeft = (int)(s/gap_size);
            if (gapsOnLeft + 1 > n)
                gapsOnLeft = n - 1;
            int gapsOnRight = n - gapsOnLeft - 2;
            double leftOffset = gap_size * gapsOnLeft;
            double rightOffset = d - gap_size * gapsOnRight;
            if (leftOffset + gap_size <= rightOffset && rightOffset >= e)
                low = gap_size;
            else
                high = gap_size;
        }
        DecimalFormat formatter = new DecimalFormat("#0.0000000000");
        System.out.println("Case #" + a + ": " + formatter.format(low));
    }
}
