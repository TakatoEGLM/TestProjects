package OOPforUnfinishedLab3;

import java.util.*;

class Item { //Where i used the concept of objects and classes
    private String pku;
    private String name;
    private String price;
    
    public Item(String pku, String name, String price) {
        this.pku = pku;
        this.name = name;
        this.price = price;
    }
    
    public String getPKU() {
        return pku;
    }
    public String getItemName() {
        return name;
    }
    public String getPrice() {
        return price;
    }
    
    @Override
    public String toString() {
        return "\nPKU: " + pku + "\nName: " + name + "\nPrice: " + price;
    }
}

class Inventory { //Inventory Methods for Employees
    public List<Item> inventory;
    
    public Inventory() {
        this.inventory = new ArrayList<>();
    }
    
    public void addItem() {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the PKU of item: ");
        String pku = input.nextLine();
        System.out.print("Enter the name of item: ");
        String name = input.nextLine();
        System.out.print("Enter the price of item: ");
        String price = input.nextLine();
        
        Item newItem = new Item(pku, name, price);
        inventory.add(newItem);
        System.out.println("\nNew Item Added:\n" + newItem);
    }
    
    public void deleteItem() {
        if (inventory.isEmpty()) {
            System.out.println("The inventory is already empty.");
        } else {
            Scanner input = new Scanner(System.in);
            System.out.print("Enter the PKU of the item to delete: ");
            String pku = input.nextLine();

            boolean itemFound = false;
            for (int i = 0; i < inventory.size(); i++) {
                if (inventory.get(i).getPKU().equals(pku)) {
                    inventory.remove(i);
                    System.out.println("The book has been deleted successfully.");
                    itemFound = true;
                    break;
                }
            }
            if (!itemFound) {
                System.out.println("The book does not exist.");
            }
        }
    }
    public void findItem(){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the name of the item: ");
        String name = input.nextLine();

        boolean itemFound = false;
        for (int i = 0; i < inventory.size(); i++) {
            if (inventory.get(i).getItemName().equalsIgnoreCase(name)) {
                System.out.println("Item " + (i) + ":");
                System.out.println(inventory.get(i));
            }
        }
    }
    
    public void viewInventory() {
        if (inventory.isEmpty()) {
            System.out.println("The inventory is empty.");
        } else {
            System.out.println("Inventory Catalog:");
            for (int i = 0; i < inventory.size(); i++) {
                System.out.println("Item " + (i + 1) + ":");
                System.out.println(inventory.get(i));
            }
        }
    }
    
    public void clearInventory() {
        if (inventory.isEmpty()) {
            System.out.println("The inventory is already empty!");
        } else {
            inventory.clear();
            System.out.println("All items had been cleared from the inventory!");
        }
    }
}

class Shop { //Shop Methods for clients
    private List<Item> cart;
    
    public Shop() {
        this.cart = new ArrayList<>();
    }

    public void viewCatalog(Inventory inventory) {
        inventory.viewInventory();
    }

    public void addToCart(Inventory inventory) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the PKU of the item to add to cart: ");
        String pku = input.nextLine();

        Item selectedItem = null;
        for (Item item : inventory.inventory) {
            if (item.getPKU().equals(pku)) {
                selectedItem = item;
                break;
            }
        }

        if (selectedItem != null) {
            cart.add(selectedItem);
            System.out.println("Item added to cart: " + selectedItem);
        } else {
            System.out.println("Item not found in inventory.");
        }
    }

    public void viewCart() {
        if (cart.isEmpty()) {
            System.out.println("Your cart is empty.");
        } else {
            System.out.println("Your Cart:");
            for (Item item : cart) {
                System.out.println(item);
            }
        }
    }

    public void removeFromCart() {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the PKU of the item to remove from cart: ");
        String pku = input.nextLine();

        boolean removed = cart.removeIf(item -> item.getPKU().equals(pku));
        if (removed) {
            System.out.println("Item removed from cart.");
        } else {
            System.out.println("Item not found in cart.");
        }
    }

    // Confirm purchase and show total price
    public void confirmPurchase() {
        if (cart.isEmpty()) {
            System.out.println("Your cart is empty.");
            return;
        }
        
        double total = 0;
        System.out.println("Items in your purchase:");
        for (Item item : cart) {
            System.out.println(item);
            total += Double.parseDouble(item.getPrice());
        }
        System.out.printf("Total Price: %.2f\n", total);
        
        System.out.print("Confirm purchase? (Y/N): ");
        Scanner input = new Scanner(System.in);
        String confirm = input.nextLine().toLowerCase();

        if (confirm.equals("y")) {
            System.out.println("Purchase complete, thank you!");
            cart.clear();
        } else {
            System.out.println("Purchase cancelled.");
        }
    }
}

// Where I used the concept of inheritance and composition
abstract class EmployeeUser {
    protected String username;
    
    public EmployeeUser(String username) {
        this.username = username;
    }
    public void viewInventory(Inventory inventory) {
        inventory.viewInventory();
    }
    public void findItem(Inventory inventory) {
        inventory.findItem();
    }
    
}
class Admin extends EmployeeUser {
    public Admin(String username) {
        super(username);
    }
    public void addItem(Inventory inventory) {
        inventory.addItem();
    }
    public void deleteItem(Inventory inventory) {
        inventory.deleteItem();
    }
    public void clearInventory(Inventory inventory) {
        inventory.clearInventory();
    }
}
class Operator extends EmployeeUser {
    public Operator(String username) {
        super(username);
    }
    public void addItem(Inventory inventory) {
        inventory.addItem();
    }
    public void deleteItem(Inventory inventory) {
        inventory.deleteItem();
    }
}
class Regular extends EmployeeUser {
    public Regular(String username) {
        super(username);
    }
}