package Week3;
import java.util.Scanner;

public class hw3 {
    public static void main(String[] args) {
        /*
        Write a Java program that takes the user to provide a word of any sort. 
        Print the character at the last position, capitalized, and the word's length
         (e.g. for Hotel, print L5). If a number is provided, print an error message.
        */
        Scanner scnr = new Scanner(System.in);

        String word = scnr.nextLine();
        int wordLen = word.length();
        char lastChar = word.charAt(wordLen-1);
        System.out.println(Character.toUpperCase(lastChar) + String.valueOf(wordLen));



        scnr.close();
    }
}