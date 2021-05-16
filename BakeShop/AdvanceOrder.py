
#--------------------FIT5136_SEM_02_Team 09  Assignment 4B - Bakeshop System -------------------------------
# Author Names & IDs : Dipal Vyas(31847390) , Aashna Jain(29802911) , Nivedha Balasubramanian(30729963), Kanika Bansal(31030319)
# Start Date : 16th September, 2020
# End Date : 1st November, 2020
#------------------------------------------------------------------------------------------------------------
# Class Description: AdvanceOrder.py is an inherit class of Order class which implements the functionality of ordering
#                    'Roast coffee beans' item created and handled by Owner- Oliver and Manager.

# This Class calls required variable values from order class.
# functions: 1.advance_order : The main purpose of this function is to create advance order for roast coffee beans by asking customer
#                              what quantity he wants to order and stores customer details: Name, contact number for later delivery.

#-------------------Importing libraries and classes-------------------------
import re
from Order import Order
from Item import Item
#--------------------------------------------------------------------------


class AdvanceOrder(Order):
# initialises variable and calls from order class.
    def __init__(self):
        super().__init__()

# This function is developed for user inputs(item quantiry, user contact number) for placing order and once order confirmed,
# order details is displayed and order details is stored using write function.


    def advance_order(self, store_id, new_order_num, staff_id_var, customer_name):
        flag = input("Do you want to add an item? Y/N: ")
        if flag == 'Y':
            item_name = "roast coffee beans"
            item = Item()
            self.item_detail = item.get_available_items(item_name, int(store_id))
            input_item_no = 1
            self.set_item_to_store(input_item_no)
            item_total = 0
            #Asking quantity to placce from user which should be > 0 and search the quantity in the inventory.
            # If quantity is not available then again asks user if he wants to change the quantity number.
            while True:
                input_quantity = input("Input item quantity: ")
                try:
                    input_quantity = int(input_quantity)
                    if input_quantity == 0:
                        print("Quantity cannot be 0. Please enter valid quantity")
                        pass
                    elif self.item_detail[input_item_no - 1][2] >= input_quantity > 0:
                        item_total = input_quantity * self.item_detail[input_item_no - 1][3]
                        self.set_cost_to_store(item_total)
                        self.set_quantity_to_store(input_quantity)

                        self.order_total = round(self.order_total + item_total, 2)
                        zero_qty_flag = True
                        break
                    elif self.item_detail[input_item_no - 1][2] == 0:
                        print("Quantity is not available!")
                        zero_qty_flag = False
                        break
                    else:
                        print("Quantity is not available in the inventory, " + str(
                            self.item_detail[input_item_no - 1][2]) + "  Quantity is available")
                        flag_check = input("Do you want change item quantity?(Y/N)")
                        if flag_check == 'Y':
                            input_quantity = int(input("Enter other Quantity"))

                        elif flag_check == 'N':
                            break
                except ValueError:
                    print("Incorrect Input. Please enter a valid Key value")
                    pass

            # Contact number should be asked for later delivery of an order.
            if zero_qty_flag:
                while True:
                    self.cust_contact_no = input("Enter Customer Contact Number: ")
                    # https://www.regexlib.com/Search.aspx?k=australian%20phone&AspxAutoDetectCookieSupport=1 used
                    # for the regex expression.
                    # Matches all known formats including normal 10-digit landline numbers (valid
                    # area code mandatory) 13, 1300, 1800, 1900, 1902 plus mobile 10 and 11-digit formats.
                    regex = re.compile(r'^\({0,1}((0|\+61)(2|4|3|7|8)){0,1}\){0,1}(\ ){0,1}[0-9]{2}(\ ){0,1}[0-9]{2}(\ ){'
                                       r'0,1}[0-9]{1}(\ ){0,1}[0-9]{3}$')

                    if regex.match(self.cust_contact_no):
                        break
                    else:
                        print("The Contact Number Entered is not Valid! The Contact Number should be Australian. "
                              "Please try again.")
        elif flag == 'N':
            pass
        else:
            print("Incorrect Input. Please enter a valid value")

        if not self.get_list_of_item() or not self.get_list_of_quantity():
            print("Order Status: Cancelled")
        else:
            # Displaying order details
            print("---------------- Order Placed ------------------")
            for (name, quant, cost) in zip(self.get_list_of_item(), self.get_list_of_quantity(),
                                           self.get_list_of_cost()):
                print("Item Name: " + str(name))
                print("Item Quantity: " + str(quant))
                print("Item Cost: " + str(cost / quant))
                print("Total Item Cost: " + str(cost))
                print("\n")
            print("----- Order Total -----")
            print("Order Total: ", self.order_total)
            print("Order Status: Confirmed")

        date, time = self.get_date_time()

        # calling write function to write order data into file
        if self.get_list_of_item() or self.get_list_of_quantity():
            self.write_order(store_id, new_order_num, staff_id_var, customer_name, 'Confirmed', self.cust_contact_no)
