package Java.CSCI.Week12;
import java.util.Scanner;

public class testing {
    public static double pyramidVolume(double baseLength, double baseWidth, double pyramidheight) {
        double baseArea = baseLength * baseWidth;
        double volume =  baseArea * pyramidheight / 3;
        return volume;
    }

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double userLength;
        double userWidth;
        double userHeight;

        userLength = scnr.nextDouble();
        userWidth = scnr.nextDouble();
        userHeight = scnr.nextDouble();
        double result = pyramidVolume(userLength, userWidth, userHeight);
        System.out.println("Volume: " + result);

        scnr.close();
    }
}