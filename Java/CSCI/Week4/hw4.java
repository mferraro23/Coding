package Java.CSCI.Week4;
import java.util.Scanner;
public class hw4{
    public static void main(String[] args) {
        // this is a single line comment
        /* 
        this is a multi-
        line comment
        */ 
        Scanner scnr = new Scanner(System.in); // for keyboard 
        String singleLine; 
        System.out.println("Enter a sentance: \n");
        singleLine = scnr.nextLine(); // gets the whole line
        int inputValue; // declaring an int
        System.out.println("Enter an Int: \n");
        inputValue = scnr.nextInt(); // convert KB entry to int
        String singleWord; // declaring string
        System.out.println("Enter a String: \n");
        singleWord = scnr.next(); // gets the next word
        double firstDouble; // declaring a double
        System.out.println("Enter a Double: ");
        firstDouble = scnr.nextDouble(); // gets the next double
        float firstFloat; // declaring a float
        System.out.println("Enter a float: \n");
        firstFloat = scnr.nextFloat(); // gets the next float
        long firstLong; // declaring a long
        System.out.println("Enter a Long: \n");
        firstLong = scnr.nextLong(); // gets the next long
        boolean firstBoolean; // declare a boolean
        System.out.println("Enter a Boolean: \n");
        firstBoolean = scnr.nextBoolean(); // gets the next Boolean
        boolean secondBoolean;
        System.out.println("Enter another Boolean: \n");
        secondBoolean = scnr.nextBoolean();
        System.out.println("\n\n\n\n\n");
        if (firstBoolean == true && secondBoolean == true){ // && means that this only evaluates to true if both statements are true
            System.out.println("The first and second Boolean are true.\n");
        }
        else if (firstBoolean == false && secondBoolean == false){
            System.out.println("The first and second boolean are false.\n");
        }
        else if (firstBoolean == true && secondBoolean == false){
            System.out.println("The first boolean is true and second boolean is false.\n");
        }
        else if (firstBoolean == false && secondBoolean == true){
            System.out.println("The first boolean is false and second boolean is true.\n");
        }

        if (firstBoolean == true || secondBoolean == false){ // either the first boolean needs to be true or the second boolean needs to false for this to evaluate to true
            System.out.println("Either the first boolean is true or the second boolean is false.\n");
        }
        else if (firstBoolean == false || secondBoolean == true){
            System.out.println("Either the first boolean is false or the second boolean is true.\n");
        }

        /*
        If statement, if the inside is true then it executes the contents of the curley brackets.
        If else statement, if the first if statement is false it will move to the next else if statement.
        */

        if (inputValue % 2 != 0){ // != means that it is not equal to. % is used to see if there is a remainder. This checks if it is even or odd
            System.out.println("The integer " + inputValue + " is an odd number.\n");
        }
        else{
            System.out.println("The integer " + inputValue + " is an even number.\n");
        }

        int charVal = 100;
        char letter;
        while (charVal>=singleWord.length()){
            System.out.println("Enter a number to find the character at in the word " + singleWord + ".\n");
            charVal = scnr.nextInt();
        }
        
        letter = singleWord.charAt(charVal); // charAt finds the char at the index given.
        System.out.println("The letter at index " + charVal + ", in the word " + singleWord + ", is " + letter + ".\n");
        
        firstDouble = 4 * 4.0; // type cast int to double
        System.out.println("This is a double: " + firstDouble + ". \n" + "This is the square root of the double: " + Math.sqrt(firstDouble) + ".\nThis is the double squared: " + Math.pow(firstDouble, 2) + ".\n");

        String subLine;
        subLine = singleLine.substring(3); //Gets the substring starting at the third index
        System.out.println(subLine + ". This is the substring of the full word " + singleLine + ".\n A long is " + firstLong + ". A float is not a good way to store a decimal point but this is a float " + firstFloat + ".");
        
        scnr.close();
    }
}