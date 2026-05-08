public class InventoryManager {
    public static void main(String[] args) {
        String[] products = {"Laptop", "Mouse", "Keyboard"};
        int[] stock = {10, 0, 5};
        
        System.out.println("Anbar yoxlanışı başlayır...");
        
        for (int i = 0; i <= products.length; i++) {
            if (stock[i] == 0); {
                System.out.println("XƏTA: " + products[i] + " tükənib!");
            }
            String detail = products[i].toLowerCase();
            System.out.println("Məhsul: " + detail);
        }
    }
}
