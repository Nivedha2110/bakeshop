'''
--------------------FIT5136_SEM_02_Team 09  Assignment 4B - Bakeshop System -------------------------------
Author Names & IDs : Dipal Vyas(31847390) , Aashna Jain(29802911) , Nivedha Balasubramanian(30729963), Kanika Bansal(31030319)
Start Date : 16th September, 2020
End Date : 1st November, 2020
------------------------------------------------------------------------------------------------------------
Class Description: BakeShopSystem.py is the controller class in this system and the overall program starts running from this class
This Class calls required methods from other classes
------------------------------------------------------------------------------------------------------------
'''

from Employee import Employee
from Order import Order
from Item import Item
from AdvanceOrder import AdvanceOrder
from datetime import datetime
from Report import Report
from UserInterface import UserInterface
from Inventory import Inventory
from calendar import monthrange

user_interface = UserInterface()


class BakeShopSystem:

    # Check username and password
    def verify_login(self, user, pswd):
        employee = Employee()
        password = employee.get_emp_password(user)
        if password == pswd:
            return True
        else:
            print("Your username and/or password was incorrect, Please login again")
            return False

    # Retrieve the date range for last month
    def last_month_dates(self):
        last_month = datetime.today().month - 1
        year_now = datetime.today().year
        first_day = monthrange(year_now, last_month)[0]
        last_day = monthrange(datetime.today().year, datetime.today().month - 1)[1]

        print("Date range: " + str(first_day) + "/" + str(last_month) + "/" + str(year_now) + " to " + str(
            last_day) + "/" + str(last_month) + "/" + str(year_now))
    # create a new order
    def create_order(self, user):
        date_time = datetime.now()
        date = date_time.strftime("%d/%m/%Y")
        time = date_time.strftime("%H:%M:%S")
        order = Order()
        employee = Employee()
        advance_order = AdvanceOrder()

        # get the staff ID from Employer class
        staff_id_var = employee.get_emp_id(user)

        print("Bakeshop")
        print("Create Order")
        print('')
        print("Staff ID:", staff_id_var)

        # Get the store ID for the current order
        store_id = employee.get_emp_store_id(user)

        # Generate a new order ID for this order
        new_order_num = order.get_order_id()

        print("Store ID:", store_id)
        print("Order Date:", date)
        print("Order Time:", time)
        print("Order ID:", new_order_num)
        print('')
        print("Enter Order Details below:")

        # Take customer name as input and verify the input value
        while True:
            cust_name = input("Customer's Name: ")
            if cust_name.replace(' ', '').isalpha():
                break
            else:
                print("Invalid customer name. Please enter again")

        while True:
            try:
                order_type = input("Please choose order type: 1 for Current Order and 2 for Advance Order: ")
                if order_type.isdigit():

                    # Current Order
                    if (order_type == '1'):
                        self.normal_order(store_id, new_order_num, staff_id_var, cust_name)
                        break

                    # Advance order
                    elif (order_type == '2'):
                        advance_order.advance_order(store_id, new_order_num, staff_id_var, cust_name)
                        break
                    else:
                        print("Incorrect Input. Please try again.")
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input")

        print("Press 1 to place another Order")
        print("Press 2 to go to the homepage")

        # Input for the menu option and its validation
        while True:
            try:
                input_1 = str(input("Please Select Your Operation: "))
                if input_1.isdigit():
                    if len(input_1) == 1:
                        if input_1 == '1':
                            self.create_order(user)
                        elif input_1 == '2':
                            self.homepage(user)
                        else:
                            print("Select proper option")
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input! Please Try Again.")

    def normal_order(self, store_id, new_order_num, staff_id_var, customer_name):
        order = Order()
        date, time = order.get_date_time()
        while (True):
            # Ask the user if item needs to be added
            flag = input("Do you want to add an item? Y/N: ").upper()
            # make item object here
            if (flag == 'Y'):

                while True:
                    # Take item details as input and apply validation checks

                    item_name = input("Enter item name: ")
                    if item_name.replace(' ', '').isalpha():
                        item_name = item_name.lower()
                        break
                    else:
                        print("Invalid item name. Please try again")

                item = Item()

                # Get list of items matching with the input item name and print the list
                order.item_detail = item.get_available_items(item_name, int(store_id))
                for item_to_print in order.item_detail:
                    print(str(item_to_print[0]) + '. ' + str(item_to_print[1]))
                if order.item_detail:
                    while True:
                        # Ask user to select an option number from list of items
                        input_item_no = input("Enter option number for the Item you want to select: ")
                        if input_item_no.isdigit():
                            break
                        else:
                            print("Invalid Input! Please try again!")
                    try:
                        input_item_no = int(input_item_no)
                        if len(order.item_detail) < input_item_no:
                            print("Incorrect Item number selection. Please try again")
                            pass
                        else:
                            # Save the item in the order if available and ask for quantity
                            order.set_item_to_store(input_item_no)
                            item_total = 0
                            while (True):
                                input_quantity = input("Input item quantity: ")
                                try:
                                    input_quantity = int(input_quantity)
                                    if input_quantity == 0:
                                        print("Quantity cannot be 0. Please enter valid quantity")
                                        pass

                                    # If the item is not available, inform the user and ask to select anther item
                                    elif order.item_detail[input_item_no - 1][2] == 0:
                                        print("Quantity Not Available!")
                                        break
                                    elif order.item_detail[input_item_no - 1][2] >= input_quantity > 0:
                                        item_total = input_quantity * order.item_detail[input_item_no - 1][3]
                                        item.update_quantity_order(store_id, (order.item_detail[input_item_no - 1][1]),
                                                                   input_quantity, order.item_detail[input_item_no - 1][2])
                                        order.set_cost_to_store(item_total)
                                        order.set_quantity_to_store(input_quantity)

                                        order.order_total = round(order.order_total + item_total, 2)
                                        break
                                    else:
                                        # If the input quantity is not available, inform the user and ask for another quantity
                                        print("Quantity is not available in the inventory, " + str(
                                            order.item_detail[input_item_no - 1][2]) + "  Quantity is available")
                                        flag_check = input("Do you want change item quantity?(Y/N)")
                                        if (flag_check == 'Y'):
                                            input_quantity = float(input("Enter other Quantity"))
                                        elif (flag_check == 'N'):
                                            break
                                except ValueError:
                                    print("Incorrect Input. Please enter a valid Key value")
                                    pass
                    except ValueError:
                        print("Incorrect Input. Please enter a valid Key value")
                        pass
                else:
                    print("No Item found")
            elif (flag == 'N'):
                break
            else:
                print("Incorrect Input. Please enter a valid value")

        if order.get_list_of_item() or order.get_list_of_quantity():
            # calling write function to write order data into file
            order.write_order(store_id, new_order_num, staff_id_var, customer_name, 'Confirmed', '')

            # Order cancelled if no valid items entered or if quantity of item not found
            if not order.get_list_of_item() or not order.get_list_of_quantity():
                print("Order Status: Cancelled")
            else:
                print("---------------- Order Placed ------------------")
                for (name, quant, cost) in zip(order.get_list_of_item(), order.get_list_of_quantity(),
                                               order.get_list_of_cost()):
                    print("Item Name: " + str(name))
                    print("Item Quantity: " + str(quant))
                    print("Item Cost: " + str(cost / quant))
                    print("Total Item Cost: " + str(round(cost, 2)))
                    print("\n")
                print("----- Order Total -----")
                print("Order Total: ", order.order_total)
                print("Order Status: Confirmed")

    # function to get total coffee beans sold in last month in each store
    def get_coffee_bean_report(self):
        report = Report()
        report.get_total_coffee_beans_sold()

    # function to get total food items sold in last month in each store
    def get_total_food_items_sold(self):
        report = Report()
        report.get_total_number_of_items()

    # function to get days of the week with most items sold in last month in each store
    def get_days_of_week_sale(self):
        report = Report()
        report.get_days_of_week_most_sale()

    # function to get total coffee items sold in last month in each store
    def get_total_coffee_items_sold(self):
        report = Report()
        report.get_total_number_of_coffee()

    # function to get total coffee types sold in last month in each store
    def get_total_coffee_type_sold(self):
        report = Report()
        report.get_coffe_type_sold()

    # function to get items low in inventory in the last week in each store
    def get_low_in_inventory(self):
        report = Report()
        report.get_low_in_inventory()

    # function to get total sale made in last month in each store
    def get_sale_made_in_month(self):
        report = Report()
        report.get_sale_made_in_month()

    # function to add an item in the inventory
    def add_inventory(self, user):

        employee = Employee()
        # Get the store ID for the current order
        store_id = employee.get_emp_store_id(user)

        inventory = Inventory()
        item = Item()
        # Get current date and time
        date_time = datetime.now()
        date = date_time.strftime("%m/%d/%Y")

        while True:
            # Get item name and apply input validation
            partial_name = input("Enter item name: ")
            if partial_name.replace(' ', '').isalpha():
                partial_name = partial_name.lower()
                break
            else:
                print("Invalid item name. Please try again")

        # Get list of items matching the input item name and print the list
        item_detail = item.get_available_items_inv(partial_name, int(store_id))
        for item_to_print in item_detail:
            print(str(item_to_print[0]) + '. ' + str(item_to_print[1]))

        if item_detail:
            while True:
                try:
                    input_item_no = int(input("Enter option number for the Item you want to select: "))
                    item_name = item_detail[input_item_no - 1][1]
                    break
                except (ValueError, IndexError):
                    print("Invalid Input!")
                    pass
                while True:
                    try:
                        quantity_added = input("Enter quantity to be added: ")
                        if quantity_added.isdigit():
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid Input!")
                        pass
                item_id = item.get_item_id(item_name)
                quantity = int(float(item.get_quantity(item_name, store_id)))

                # Update the inventory with the provided item and its quantity details
                item.update_quantity_inv(store_id, item_name, quantity_added, quantity)
                inventory.write_inventory(store_id, item_id, item_name, quantity_added, date)

                print('*' * 81)
                print(" INVENTORY ADDED ")
        else:
            print("NO ITEM FOUND")


    # User login function to take input username and password
    def login(self):
        user_interface.display_login_option()
        username = input("Enter your username (email-address): ")
        if username != "":
            password = input("Enter your password: ")
            if password == '':
                print("Please enter a proper password")
                self.login()

            # Verify if the entered credentials are correct
            verify_login = self.verify_login(username, password)
            if verify_login == False:
                self.login()
            else:
                self.homepage(username)
        else:
            print("Please enter a proper username")
            self.login()

    # Home page displayed after successful login
    def homepage(self, user):
        employee = Employee()
        employee_name = employee.get_emp_name(user)
        user_interface.display_main_menu(employee_name)
        user_type = employee.get_emp_user_type(user)

        # Display main menu options depending on user type
        while True:
            if user_type == "Owner":
                user_interface.display_owner_homepage()
            elif user_type == "Manager":
                user_interface.display_manager_homepage()
            else:
                user_interface.display_homepage()

            # Options Handling : 1-2-3-4-5.
            input_1 = str(input("Please Select Your Operation: "))
            if len(input_1) == 1:
                # Easy Access Checking Logic
                if input_1 == '1':
                    print("\n" * 1)
                    # Show Order Menu
                    self.order(user)
                    break
                elif input_1 == '2':
                    if user_type == "Owner" or user_type == "Manager":
                        # Only owner and manager can update the inventory
                        self.inventory_menu(user)
                    break

                elif input_1 == '3':
                    if user_type == "Owner":
                        # only owner can view the reports
                        self.report_menu(user)
                        break
                    else:
                        print("*" * 32 + " YOU HAVE SUCCESSFULLY LOGGED OUT " + "*" * 31 + "\n")
                        self.login()
                elif input_1 == '4':
                    # Logout functionality
                    if user_type == "Owner":
                        print("*" * 32 + " YOU HAVE SUCCESSFULLY LOGGED OUT " + "*" * 31 + "\n")
                        self.login()
                    break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Handling Bad Inputs
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    # displays the order menu
    def order(self, user):
        while True:
            user_interface.display_order_main()
            input_1 = str(input(" Please Select Your Operation: "))  # Options Handling : 1-2-3-4-5.
            if len(input_1) == 1:
                if input_1 == '1':  # Easy Access Checking Logic
                    print("\n" * 2)
                    self.create_order(user)
                    break
                elif input_1 == '2':
                    print("\n" * 1)
                    self.homepage(user)
                    break
                else:
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  # Handling Bad Inputs
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    # displays the inventory menu
    def inventory_menu(self, user):
        while True:
            user_interface.display_inventory_menu()
            input_2 = str(input("Please Select Your Operation: "))
            if len(input_2) == 1:
                if input_2 == '1':  # Easy Access Checking Logic
                    print("\n" * 1)
                    print("-" * 81)
                    self.add_inventory(user)
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to Inventory Menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.inventory_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                elif input_2 == '2':
                    self.homepage(user)
                    break
                else:
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")

    # displays the report menu

    def report_menu(self, user):
        while True:
            user_interface.display_report_menu()
            input_2 = str(input("Please Select Your Operation: "))
            if len(input_2) == 1:
                if input_2 == '1':  # Easy Access Checking Logic
                    print("\n" * 1)
                    print("Low in inventory at the end of each week in each store ")
                    print("-" * 81)
                    self.get_low_in_inventory()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to Report Menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                elif input_2 == '2':
                    print("\n" * 1)
                    print("Total Number of Coffee Sold Last Month in each store: ")
                    self.last_month_dates()
                    print("-" * 81)
                    self.get_total_coffee_items_sold()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to report menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                elif input_2 == '3':  # Easy Access Checking Logic
                    print("\n" * 1)
                    print("Total Coffee Beans Sold In Last Month in each store: ")
                    self.last_month_dates()
                    print("-" * 81)
                    self.get_coffee_bean_report()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to report menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                    # break
                elif input_2 == '4':
                    print("\n" * 1)
                    print("Total Food Items Sold In Last Month in each store: ")
                    self.last_month_dates()
                    print("-" * 81)
                    self.get_total_food_items_sold()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to report menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                    # break

                elif input_2 == '5':
                    print("\n" * 1)
                    print("Type of Coffee Sold the most Last Month in each store: ")
                    self.last_month_dates()
                    print("-" * 81)
                    self.get_total_coffee_type_sold()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to report menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                elif input_2 == '6':
                    print("\n" * 1)
                    print("Days of the week that made the most sale in the last month in each store")
                    self.last_month_dates()
                    print("-" * 81)
                    self.get_days_of_week_sale()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to report menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                elif input_2 == '7':
                    print("\n" * 1)
                    print("Total sale made in dollars in the last month per store ")
                    self.last_month_dates()
                    print("-" * 81)
                    self.get_sale_made_in_month()
                    print('*' * 81)
                    while True:
                        input_3 = str(input("Press 1 to go back to report menu: "))
                        if len(input_3) == 1:
                            if input_3 == '1':
                                self.report_menu(user)
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                    input_3) + "). Try again!")  # Handling Bad Inputs
                        else:
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(
                                input_3) + "). Try again!")  # Handling Bad Inputs
                elif input_2 == '8':
                    print("\n" * 1)
                    self.homepage(user)
                    break
                else:
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(
                        input_2) + "). Try again!")  # Handling Bad Inputs
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")


# Code starts from the BakeShopSystem class as this is the controller class
if __name__ == "__main__":
    ui_object = BakeShopSystem()
    ui_object.login()
