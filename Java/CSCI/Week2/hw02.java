package Java.CSCI.Week2;
import java.util.Scanner;

public class hw02 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        System.out.println("Enter 3 numbers...");

        int num1 = scnr.nextInt();
        int num2 = scnr.nextInt();
        int num3 = scnr.nextInt();
        double avg;

        avg = (double)(num1 + num2 + num3) / 3;
        System.out.printf("Your average is: " + "%.3f", avg);
        System.out.println(" ");
        
        scnr.close();
    }
}