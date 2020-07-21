import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class queens
{
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(System.in);
       // var input = new Scanner(new File("1.in"));

        int test = input.nextInt();
        for (int x = 1; x < test+1; x++)
        {
            int size = input.nextInt();
            int[][]board = new int[size][size];
            ArrayList<Integer>filled_columns = new ArrayList<>();
            for (int j = 0; j < size; j++)
            {
                String row = input.next();
                for (int k = 0; k < row.length(); k++)
                {
                    char dummy = row.charAt(k);
                    if(dummy == 'x')
                    {
                        board[j][k] = 1;
                        filled_columns.add(k);
                    }
                }
            }

            boolean illegal = illdefinedProblem(board);
            System.out.println("Case #" + x + ": ");

            if(!illegal && Queen(board , filled_columns , 0))
            {
                for (int k = 0; k < board.length; k++)
                {
                    for (int m = 0; m < board.length; m++)
                    {
                        if(board[k][m] == 1)
                            System.out.print("x");
                        else
                            System.out.print(".");

                    }
                    System.out.println();
                }
            }
            else
                System.out.println("impossible");
        }
        input.close();
    }

    public static boolean illdefinedProblem(int[][]board)
    {
        boolean ill_defined = false;
        for (int j=0; j<board.length; j++) //for row check!!!
        {
            int[]temp = board[j];
            int count = 0;
            for (int k = 0; k < temp.length; k++)
            {
                if(temp[k] == 1)
                    count++;

            }
            if(count>1)
            {
                ill_defined = true;
                break;
            }
        }

        if(!ill_defined)//for column check!!!
            for (int j = 0; j<board.length; j++)
            {
                int count = 0;
                for (int k = 0; k < board.length; k++)
                {
                    if(board[k][j] == 1){
                        count++;
                    }
                }
                if(count>1) {
                    ill_defined = true;
                    break;
                }
            }

        if(!ill_defined)  //diagonal check!!!
            for (int j = 0; j<board.length; j++)
            {
                for (int k = 0; k < board.length; k++)
                {
                    if(board[j][k]==1)
                    {
                        for (int row=j+1,  col=k+1 ; row<board.length && col<board.length; row++,col++) // go to the right down diagonal part
                        {
                            if(board[row][col]==1)
                            {
                                ill_defined = true;
                                break;
                            }
                        }
                        for (int row=j+1, col=k-1 ; row<board.length && col>=0; row++,col--) // go to the left down diagonal part
                        {
                            if(board[row][col]==1)
                            {
                                ill_defined = true;
                                break;
                            }
                        }
                    }
                }
            }

        return ill_defined;
    }


    public static boolean Queen(int[][]board , ArrayList<Integer>filled , int col)
    {
        while(filled.contains(col))
            col++;

        if(col >= board.length)
        {
            return true;
        }
        for (int i = 0; i < board.length; i++)
        {
            if(isSafe(board , i , col))
            {
                board[i][col] = 1;
                if(Queen(board , filled , col+1))
                    return true;

                if(!filled.contains(col))
                    board[i][col] = 0;
            }
        }
        return false;
    }

    public static boolean isSafe(int board[][], int row, int col)
    {
        //row check
        for (int i = 0; i < board.length; i++)
            if (board[row][i] == 1)
                return false;

        /*  upper diagonal on left  */
        for (int i=row,  j=col; i>=0 && j>=0; i--, j--)
            if (board[i][j] == 1)
                return false;

        /*  lower diagonal on left side */
        for (int i=row,  j=col; j>=0 && i<board.length; i++, j--)
            if (board[i][j] == 1)
                return false;

        // check right down diagonal
        for (int i=row,   j=col; i<board.length && j<board.length; i++, j++)
            if (board[i][j] == 1)
                return false;

        //check right up diagonal
        for (int i=row, j=col; i>=0 && j<board.length; i--, j++)
            if (board[i][j] == 1)
                return false;


        return true;
    }
}


