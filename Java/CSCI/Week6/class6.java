package Java.CSCI.Week6;
import java.util.Scanner;

public class class6 {
    public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int guess, answer;
      guess = 0;
      answer = 5;
      
      int guesses = 0;

      while(guess != answer){
          System.out.println(("Enter your guess: "));
          guess = scnr.nextInt();
          guesses = guesses + 1;
      }
      System.out.println("It took you " + guesses + " guesses to guess the answer.\n");

      scnr.close();
    }
}
