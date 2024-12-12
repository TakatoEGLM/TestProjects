from Mainsystem import *

class MainApplication:
    @staticmethod
    def get_num_input():
        while True:
            try:
                return int(input())
            except ValueError:
                print("Invalid input. Please enter a valid integer: ", end='')

    @staticmethod
    def main():
        inventory = Inventory()
        shop = Shop()

        while True:
            print("Are you a Client or Employee?")
            print("1. Client")
            print("2. Employee")
            print("\n0. Exit Program")
            print("\nChoice: ", end='')
            user_type = MainApplication.get_num_input()

            if user_type == 1:
                MainApplication.client_menu(shop, inventory)
            elif user_type == 2:
                print("Select Employee Role:")
                print("1. Admin")
                print("2. Operator")
                print("3. Regular")
                print("\nChoice: ", end='')
                role_type = MainApplication.get_num_input()

                if role_type == 1:
                    username = input("Enter Admin username: ")
                    password = input("Enter Admin password: ")

                    if username == "admin" and password == "admin123":
                        employee = Admin(username)
                        MainApplication.employee_menu(employee, inventory)
                    else:
                        print("\nInvalid Admin credentials.\n")
                elif role_type == 2:
                    username = input("Enter Operator username: ")
                    password = input("Enter Operator password: ")

                    if username == "operator" and password == "operator123":
                        employee = Operator(username)
                        MainApplication.employee_menu(employee, inventory)
                    else:
                        print("\nInvalid Operator credentials.\n")
                elif role_type == 3:
                    employee = Regular("regular")
                    MainApplication.employee_menu(employee, inventory)
                else:
                    print("\nInvalid role selection.\n")
            elif user_type == 0:
                break
            else:
                print("\nInvalid choice. Please select 1 or 2.\n")

    @staticmethod
    def client_menu(shop, inventory):
        while True:
            print("\n===Shop Menu===\n")
            print("1. View Shop Catalog")
            print("2. Add Item to Cart")
            print("3. View Cart")
            print("4. Remove Item from Cart")
            print("5. Confirm Purchase")
            print("\n0. Cancel")
            print("\nChoice: ", end='')
            choice = MainApplication.get_num_input()

            if choice == 1:
                shop.view_catalog(inventory)
            elif choice == 2:
                shop.add_to_cart(inventory)
            elif choice == 3:
                shop.view_cart()
            elif choice == 4:
                shop.remove_from_cart()
            elif choice == 5:
                shop.confirm_purchase()
            elif choice == 0:
                print("...Returning to main menu.")
                return
            else:
                print("\nInvalid choice.\n")

    @staticmethod
    def employee_menu(employee, inventory):
        is_admin = isinstance(employee, Admin)
        is_operator = isinstance(employee, Operator)

        while True:
            print("\n===Inventory Menu===\n")
            print("1. View Inventory Catalog")
            print("2. Find Item")
            if is_admin or is_operator:
                print("3. Add Item")
                print("4. Delete Item")
            if is_admin:
                print("5. Clear Inventory")
            print("\n0. Logout")
            print("\nChoice: ", end='')
            choice = MainApplication.get_num_input()

            if choice == 1:
                employee.view_inventory(inventory)
            elif choice == 2:
                employee.find_item(inventory)
            elif choice == 3 and (is_admin or is_operator):
                employee.add_item(inventory)
            elif choice == 4 and (is_admin or is_operator):
                employee.delete_item(inventory)
            elif choice == 5 and is_admin:
                employee.clear_inventory(inventory)
            elif choice == 0:
                print("Logging out...")
                return
            else:
                print("Invalid choice.\n")
