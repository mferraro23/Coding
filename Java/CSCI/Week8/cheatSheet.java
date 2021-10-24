package Java.CSCI.Week8;
import java.util.Scanner;

public class cheatSheet{
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int[] arr = new int[10]; //declare an array with 10 elements accessable from 0-9 
        int[][] twoDimensionArr = new int[3][5]; //declare a two-dimensional array with 3 rows and 5 columns 
        int currPower;
        char userChar;
        String[] nameArry = new String[3];

        // Setting player names
        nameArry[0] = "Mike";
        nameArry[1] = "John";
        nameArry[2] = "Chloe";

        for (int i = 0; i < arr.length; i++){
            arr[i] = scnr.nextInt(); //assing user input to array
        }

        for (int i = 0; i < twoDimensionArr.length; i++){
            for (int j = 0; j < twoDimensionArr.length; j++){
                twoDimensionArr[i][j] = scnr.nextInt();
            }
        }

        for (String names: nameArry){ // enhanced for loop 
            System.out.print(names);
        }

        currPower = 2;
        userChar = 'y';
 
        while (userChar == 'y') {
            System.out.println(currPower);
            currPower = currPower * 2;
            userChar = scnr.next().charAt(0);
        }

        System.out.println(twoDimensionArr + " " + arr);

        scnr.close();
    }
}