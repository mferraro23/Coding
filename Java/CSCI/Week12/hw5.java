package Java.CSCI.Week12;

import java.util.Scanner;

public class hw5{

    public static int[] reverseArr(int[] arr) {
        int[] tempArr = new int[arr.length];
        int j = 0;
        for (int i=arr.length-1;i>=0;i--){
            tempArr[j] = arr[i];
            j++;
        }
        for (int i=0;i<tempArr.length;i++){
            arr[i] = tempArr[i];
        }
        return arr;
    }
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int num_of_vals = scnr.nextInt();
        int[] arr = new int[num_of_vals];
        int [] copyArr = new int[num_of_vals];

        for (int i=0;i<arr.length;i++){
            arr[i] = scnr.nextInt();
        }
        copyArr = arr.clone();
        System.out.print("The normal array is: ");
        for (int i=0;i<copyArr.length;i++){
            System.out.print(copyArr[i]);
        }
        System.out.println();
        reverseArr(arr);
        System.out.print("The array reversed is: ");
        for (int i=0; i<arr.length;i++){
            System.out.print(arr[i]);
        }
        System.out.println();
        /*
        if wanted each element to be on a new line then do
        for (int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
        */
        scnr.close();
    }
    
}