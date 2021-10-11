import java.util.Scanner;
/*
a program to calculate tip for solo or party
use decimal for tip percentage
*/
public class hw1{
    public static void main(String [] Args){
        Scanner scnr = new Scanner(System.in);
        
        System.out.print("Total Bill: ");
        double billPrice = scnr.nextDouble(); //get bill with tax
        int people;
        double tipRate; //tip rate in decimal form ex: .2 is 20%
        double tipTotal; //tip total
        String numPeople = "How many people are in your party? (If alone say 1)";
        String tip = "Your total tip will be: $";
        String bill = "Your total bill will now be: $";
        String tipAmount = "What percent do you want to tip? (Write as a decimal) ";
        
        //if there is multiple parties they will split the bill
        System.out.println(numPeople);
        
        people = scnr.nextInt();

        if (people>1){
            double partysPrice = Math.round((billPrice / people)*100.0) / 100.0;
            System.out.println(tipAmount);
            tipRate = scnr.nextDouble();
            tipTotal = Math.round((tipRate * partysPrice)*100.0) / 100.0;
            System.out.println(tip + tipTotal + " at a " + (Math.round(tipRate*100)) + "% rate.");
            System.out.println(bill + (tipTotal + partysPrice));
        }
        else{
            System.out.println(tipAmount);
            tipRate = scnr.nextDouble();
            tipTotal = Math.round((tipRate * billPrice)*100.0) / 100.0;
            System.out.println(tip + tipTotal + " at a " + (Math.round(tipRate*100)) + "% rate.");
            System.out.println(bill + (tipTotal + billPrice));
        }
        System.out.println("We hope you enjoyed your meal!");
        scnr.close();
    }
}