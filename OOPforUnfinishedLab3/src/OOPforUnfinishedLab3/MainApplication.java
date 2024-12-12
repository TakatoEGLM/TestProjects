package OOPforUnfinishedLab3;

import java.util.Scanner;

public class MainApplication {
    public static int getNumInput() { //A function to get a number input, built to handle the NumberFormatException.
        Scanner sc = new Scanner(System.in);
        int number = 0;
        boolean validInput = false;

        while (!validInput) {
            String input = sc.nextLine();
            try {
                number = Integer.parseInt(input);
                validInput = true;
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a valid integer: ");
            }
        }
        return number;
    }
    public static void main(String[] args) { //Main Application
        Inventory inventory = new Inventory();
        Shop shop = new Shop();
        Scanner input = new Scanner(System.in);
        
        while (true) { // C/E Loop Decision
            System.out.println("Are you a Client or Employee?");
            System.out.println("1. Client");
            System.out.println("2. Employee");
            System.out.println("\n0. Exit Program");
            System.out.print("\nChoice: ");
            int userType = getNumInput();

            if (userType == 1) { // for client
                clientMenu(shop, inventory);
            } else if (userType == 2) { //for employees
                System.out.println("Select Employee Role:"); //Employee role decision
                System.out.println("1. Admin");
                System.out.println("2. Operator");
                System.out.println("3. Regular");
                System.out.print("\nChoice: ");
                int roleType = getNumInput();
                input.nextLine();

                EmployeeUser employee;
                
                if (roleType == 1) {
                    // Login for Admin
                    System.out.print("\nEnter Admin username: ");
                    String username = input.nextLine();
                    System.out.print("Enter Admin password: ");
                    String password = input.nextLine();

                    if (username.equals("admin") && password.equals("admin123")) {
                        employee = new Admin(username);
                        employeeMenu(employee, inventory);
                    } else {
                        System.out.println("\nInvalid Admin credentials.\n");
                    }
                } else if (roleType == 2) {
                    // Login for Operator
                    System.out.print("\nEnter Operator username: ");
                    String username = input.nextLine();
                    System.out.print("Enter Operator password: ");
                    String password = input.nextLine();

                    if (username.equals("operator") && password.equals("operator123")) {
                        employee = new Operator(username);
                        employeeMenu(employee, inventory);
                    } else {
                        System.out.println("\nInvalid Operator credentials.\n");
                    }
                } else if (roleType == 3) {
                    // No Login Required for Regular User
                    employee = new Regular("regular");
                    employeeMenu(employee, inventory);
                } else {
                    System.out.println("\nInvalid role selection.\n");
                }
            } else if (userType == 0) {
                break;
            } else {
                System.out.println("\nInvalid choice. Please select 1 or 2.\n");
            }
        }
    }

    // Shop Menu
    public static void clientMenu(Shop shop, Inventory inventory) {
        Scanner input = new Scanner(System.in);
        while (true) {
            System.out.println("\n===Shop Menu===\n");
            System.out.println("1. View Shop Catalog");
            System.out.println("2. Add Item to Cart");
            System.out.println("3. View Cart");
            System.out.println("4. Remove Item from Cart");
            System.out.println("5. Confirm Purchase");
            System.out.println("\n0. Cancel");
            System.out.print("\nChoice: ");
            int choice = getNumInput();
            
            switch (choice) {
                case 1 -> shop.viewCatalog(inventory);
                case 2 -> shop.addToCart(inventory);
                case 3 -> shop.viewCart();
                case 4 -> shop.removeFromCart();
                case 5 -> shop.confirmPurchase();
                case 0 -> {
                    System.out.println("...Returning to main menu.");
                    return;
                }
                default -> System.out.println("\nInvalid choice.\n");
            }
        }
    }

    // Inventory Menu
    public static void employeeMenu(EmployeeUser employee, Inventory inventory) {
        Scanner input = new Scanner(System.in);
        boolean isAdmin = employee instanceof Admin;
        boolean isOperator = employee instanceof Operator;

        while (true) {
            System.out.println("\n===Inventory Menu===\n");
            System.out.println("1. View Inventory Catalog");
            System.out.println("2. Find Item");
            if (isAdmin || isOperator) {
                System.out.println("3. Add Item");
                System.out.println("4. Delete Item");
            }
            if (isAdmin) {
                System.out.println("5. Clear Inventory");
            }
            System.out.println("\n0. Logout");
            System.out.print("\nChoice: ");
            int choice = getNumInput();
            
            switch (choice) {
                case 1 -> employee.viewInventory(inventory);
                case 2 -> employee.findItem(inventory);
                case 3 -> {
                    if (isAdmin || isOperator) ((Admin) employee).addItem(inventory);
                    else System.out.println("Unauthorized action.\n");
                }
                case 4 -> {
                    if (isAdmin || isOperator) ((Admin) employee).deleteItem(inventory);
                    else System.out.println("Unauthorized action.\n");
                }
                case 5 -> {
                    if (isAdmin) ((Admin) employee).clearInventory(inventory);
                    else System.out.println("Unauthorized action.\n");
                }
                case 0 -> {
                    System.out.println("Logging out...");
                    return;
                }
                default -> System.out.println("Invalid choice.\n");
            }
        }
    }
}
