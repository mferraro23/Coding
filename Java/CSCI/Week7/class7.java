package Java.CSCI.Week7;
import java.util.Scanner;

public class class7 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String msg = scnr.nextLine();
        int stringLength = msg.length();
        String newString = "";
        while(!msg.equals("done") && !msg.equals("d") && !msg.equals("Done")){
            for (int i = stringLength-1; i >= 0; i-- ){
                newString = newString + msg.charAt(i);
            }
            System.out.println(newString);
            msg = scnr.nextLine();
            stringLength = msg.length();
            newString = "";
        }
        
        scnr.close();
    }
}       
