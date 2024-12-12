class Item:
    def __init__(self, pku, name, price):
        self.pku = pku
        self.name = name
        self.price = price

    def __str__(self):
        return f"\nPKU: {self.pku}\nName: {self.name}\nPrice: {self.price}"

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self):
        pku = input("Enter the PKU of item: ")
        name = input("Enter the name of item: ")
        price = input("Enter the price of item: ")

        new_item = Item(pku, name, price)
        self.inventory.append(new_item)
        print("\nNew Item Added:\n", new_item)

    def delete_item(self):
        if not self.inventory:
            print("The inventory is already empty.")
            return
        pku = input("Enter the PKU of the item to delete: ")

        item_found = False
        for i, item in enumerate(self.inventory):
            if item.pku == pku:
                del self.inventory[i]
                print("The item has been deleted successfully.")
                item_found = True
                break
        if not item_found:
            print("The item does not exist.")

    def find_item(self):
        name = input("Enter the name of the item: ")
        for item in self.inventory:
            if item.name.lower() == name.lower():
                print(item)

    def view_inventory(self):
        if not self.inventory:
            print("The inventory is empty.")
        else:
            print("Inventory Catalog:")
            for item in self.inventory:
                print(item)

    def clear_inventory(self):
        if not self.inventory:
            print("The inventory is already empty!")
        else:
            self.inventory.clear()
            print("All items have been cleared from the inventory!")

class Shop:
    def __init__(self):
        self.cart = []

    def view_catalog(self, inventory):
        inventory.view_inventory()

    def add_to_cart(self, inventory):
        pku = input("Enter the PKU of the item to add to cart: ")

        selected_item = next((item for item in inventory.inventory if item.pku == pku), None)

        if selected_item:
            self.cart.append(selected_item)
            print("Item added to cart: ", selected_item)
        else:
            print("Item not found in inventory.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item in self.cart:
                print(item)

    def remove_from_cart(self):
        pku = input("Enter the PKU of the item to remove from cart: ")

        removed = any(item.pku == pku for item in self.cart)
        self.cart = [item for item in self.cart if item.pku != pku]

        if removed:
            print("Item removed from cart.")
        else:
            print("Item not found in cart.")

    def confirm_purchase(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        total = sum(float(item.price) for item in self.cart)
        print("Items in your purchase:")
        for item in self.cart:
            print(item)
        print(f"Total Price: {total:.2f}")

        confirm = input("Confirm purchase? (Y/N): ").lower()

        if confirm == 'y':
            print("Purchase complete, thank you!")
            self.cart.clear()
        else:
            print("Purchase cancelled.")

class EmployeeUser:
    def __init__(self, username):
        self.username = username

    def view_inventory(self, inventory):
        inventory.view_inventory()

    def find_item(self, inventory):
        inventory.find_item()

class Admin(EmployeeUser):
    def add_item(self, inventory):
        inventory.add_item()

    def delete_item(self, inventory):
        inventory.delete_item()

    def clear_inventory(self, inventory):
        inventory.clear_inventory()

class Operator(EmployeeUser):
    def add_item(self, inventory):
        inventory.add_item()

    def delete_item(self, inventory):
        inventory.delete_item()

class Regular(EmployeeUser):
    pass
