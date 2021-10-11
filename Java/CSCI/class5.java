import java.util.Scanner;

public class class5 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int a = scnr.nextInt();
        if (a > 5 && a < 10){
            System.out.println("I happened");
        }
        scnr.close();
    }
}