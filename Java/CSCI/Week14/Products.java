import java.util.ArrayList;
import java.util.Scanner;

public class Products {
    private ArrayList<Product> productList;

    public Products() {
        productList = new ArrayList<Product>();
    }

    public void inputProducts(Scanner scnr) {
        Product currProduct;
        int currPrice;
        String currName;

        currPrice = scnr.nextInt();
        while (currPrice >= 0) {
            currProduct = new Product();
            currName = scnr.next();
            currProduct.setPriceAndName(currPrice, currName);
            productList.add(currProduct);
            currPrice = scnr.nextInt();
        }
    }

    public void printAfterDiscount(int discountPrice) {
        int i;
        int currDiscountPrice;

        for (i = 0; i < productList.size(); ++i) {
            currDiscountPrice = productList.get(i).getPrice() - discountPrice;
            System.out.println("$" + currDiscountPrice + " " + productList.get(i).getName());
        }
    }
}