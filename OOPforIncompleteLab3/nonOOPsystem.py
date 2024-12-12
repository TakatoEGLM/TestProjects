inventory = []
cart = []

def get_num_input():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Invalid input. Please enter a valid integer: ", end='')

# Client functions
def view_catalog():
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory Catalog:")
        for i, item in enumerate(inventory):
            print(f"Item {i + 1}: PKU: {item['pku']}, Name: {item['name']}, Price: {item['price']}")

def add_to_cart():
    pku = input("Enter the PKU of the item to add to cart: ")
    selected_item = next((item for item in inventory if item['pku'] == pku), None)
    if selected_item:
        cart.append(selected_item)
        print("Item added to cart:", selected_item)
    else:
        print("Item not found in inventory.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        for item in cart:
            print(f"PKU: {item['pku']}, Name: {item['name']}, Price: {item['price']}")

def remove_from_cart():
    pku = input("Enter the PKU of the item to remove from cart: ")
    for item in cart:
        if item['pku'] == pku:
            cart.remove(item)
            print("Item removed from cart.")
            return
    print("Item not found in cart.")

def confirm_purchase():
    if not cart:
        print("Your cart is empty.")
        return
    total = sum(float(item['price']) for item in cart)
    print("Items in your purchase:")
    for item in cart:
        print(f"PKU: {item['pku']}, Name: {item['name']}, Price: {item['price']}")
    print(f"Total Price: {total:.2f}")
    
    confirm = input("Confirm purchase? (Y/N): ").lower()
    if confirm == 'y':
        print("Purchase complete, thank you!")
        cart.clear()
    else:
        print("Purchase cancelled.")

# Employee functions
def add_item():
    pku = input("Enter the PKU of item: ")
    name = input("Enter the name of item: ")
    price = input("Enter the price of item: ")
    inventory.append({"pku": pku, "name": name, "price": price})
    print("\nNew Item Added:", inventory[-1])

def delete_item():
    if not inventory:
        print("The inventory is already empty.")
    else:
        pku = input("Enter the PKU of the item to delete: ")
        for item in inventory:
            if item['pku'] == pku:
                inventory.remove(item)
                print("The item has been deleted successfully.")
                return
        print("The item does not exist.")

def find_item():
    name = input("Enter the name of the item: ")
    found_items = [item for item in inventory if item['name'].lower() == name.lower()]
    if found_items:
        for i, item in enumerate(found_items):
            print(f"Item {i + 1}: PKU: {item['pku']}, Name: {item['name']}, Price: {item['price']}")
    else:
        print("Item not found.")

def clear_inventory():
    if inventory:
        inventory.clear()
        print("All items have been cleared from the inventory!")
    else:
        print("The inventory is already empty.")

# Main menu and role selection
def main_menu():
    while True:
        print("Are you a Client or Employee?")
        print("1. Client")
        print("2. Employee")
        print("\n0. Exit Program")
        choice = get_num_input()
        
        if choice == 1:
            client_menu()
        elif choice == 2:
            employee_menu()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("\nInvalid choice. Please select 1 or 2.\n")

def client_menu():
    while True:
        print("\n===Shop Menu===\n")
        print("1. View Shop Catalog")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Confirm Purchase")
        print("\n0. Cancel")
        choice = get_num_input()
        
        if choice == 1:
            view_catalog()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            view_cart()
        elif choice == 4:
            remove_from_cart()
        elif choice == 5:
            confirm_purchase()
        elif choice == 0:
            print("...Returning to main menu.")
            break
        else:
            print("\nInvalid choice.\n")

def employee_menu():
    print("Select Employee Role:")
    print("1. Admin")
    print("2. Operator")
    print("3. Regular")
    role_type = get_num_input()
    if role_type == 1:
        employee_role_menu(admin=True, operator=True)
    elif role_type == 2:
        employee_role_menu(admin=False, operator=True)
    elif role_type == 3:
        employee_role_menu(admin=False, operator=False)
    else:
        print("\nInvalid role selection.\n")

def employee_role_menu(admin=False, operator=False):
    while True:
        print("\n===Inventory Menu===\n")
        print("1. View Inventory Catalog")
        print("2. Find Item")
        if admin or operator:
            print("3. Add Item")
            print("4. Delete Item")
        if admin:
            print("5. Clear Inventory")
        print("\n0. Logout")
        choice = get_num_input()
        
        if choice == 1:
            view_catalog()
        elif choice == 2:
            find_item()
        elif choice == 3 and (admin or operator):
            add_item()
        elif choice == 4 and (admin or operator):
            delete_item()
        elif choice == 5 and admin:
            clear_inventory()
        elif choice == 0:
            print("Logging out...")
            break
        else:
            print("Invalid choice or unauthorized action.\n")

main_menu()
