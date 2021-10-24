package Java.CSCI.Week2;
import java.io.IOException;
import java.util.Random;

public class hw2 {
    public static void main(String[] args) throws IOException{
        Random randGen = new Random(); 
        int randDieNum = randGen.nextInt(6)+1;
        int randDieComp = randGen.nextInt(6)+1;
        System.out.println("You Rolled a " + randDieNum + "\n");
        System.out.println("Press 'ENTER' to see what the computer rolled...");
        System.in.read();
        System.out.println("The computer rolled a " + randDieComp + "\n");
        if (randDieComp>randDieNum){
            System.out.println("That means, you lost:( \n");
        }
        else if (randDieComp<randDieNum){
            System.out.println("That means, you won!!");
        }
        else if (randDieComp == randDieNum){
            System.out.println("Well i guess that is a tie!");
        }

    }
}
