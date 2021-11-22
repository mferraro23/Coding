import java.util.Scanner;

public class testing2 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String name = "name";
        System.out.println("String to compare");
        String compare = scnr.nextLine();
        if (compare.equalsIgnoreCase(name)){
            System.out.println("it works");
        }
        else{
            System.out.println("No");
        }
        scnr.close();
    }
}
