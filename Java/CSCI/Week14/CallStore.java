import java.util.Scanner;

public class CallStore {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        Store ourPlace = new Store();
        String currName;

        currName = scnr.nextLine();
        ourPlace.setName(currName);

        ourPlace.readAllProducts(scnr);
        ourPlace.printSale(1);
    }
}