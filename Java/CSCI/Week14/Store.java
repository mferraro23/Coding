import java.util.Scanner;

public class Store {
    private String name;
    Products products;

    public Store() {
        products = new Products();
    }

    public void setName(String storeName) {
        name = storeName;
    }

    public void readAllProducts(Scanner scnr) {
        products.inputProducts(scnr);
    }

    public void printSale(int saleAmount) {
        System.out.println(name + "'s sale:");

        products.printAfterDiscount(saleAmount);
    }
}