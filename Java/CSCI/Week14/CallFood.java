public class CallFood {
    public static void main(String[] args) {
        FoodType order1 = new FoodType("Sushi");
        FoodType order2 = new FoodType("Sandwich");
        FoodType order3 = new FoodType("Lobster");
        FoodType order4 = new FoodType("Bread");
        FoodType order5 = new FoodType("Ham");

        order3.print();

        System.out.println("Next ID: " + FoodType.getNextId());
    }
}