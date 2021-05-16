'''
--------------------FIT5136_SEM_02_Team 09  Assignment 4B - Bakeshop System -------------------------------
Author Names & IDs : Dipal Vyas(31847390) , Aashna Jain(29802911) , Nivedha Balasubramanian(30729963), Kanika Bansal(31030319)
Start Date : 16th September, 2020
End Date : 1st November, 2020
------------------------------------------------------------------------------------------------------------
Class Description: UserInterface.py is the view class of the BakeShop System. This class contains all the display
options. The functions are called from BakeShopSystem
------------------------------------------------------------------------------------------------------------
'''

class UserInterface:
    #Displays main menu with banner for the employee
    def display_main_menu(self, employee_name):
        print("*" * 41 + "*" * 41 + "\n")
        print(" " * 30 + "OLIVER'S BAKESHOP" + " " * 30 + "\n")
        print("*" * 41 + "*" * 41 + "\n")
        print("")
        print("Welcome to Oliver's Bakeshop " + employee_name + "!")
        print("")

    def display_login_option(self):
        #Displays the login page for the user to login
        print("*" * 41 + "*" * 41 + "\n")
        print(" " * 30 + "OLIVER'S BAKESHOP" + " " * 30 + "\n")
        print("*" * 41 + "*" * 41 + "\n")
        print("*" * 36 + " LOGIN PAGE " + "*" * 36 + "\n")

    def display_owner_homepage(self):
        #Displays the homepage if the user is of owner user type
        print("*" * 36 + " HOME PAGE " + "*" * 36 + "\n"  # Order Main Menu
                                                    "\t(1) ORDER MENU\n"
                                                    "\t(2) INVENTORY\n"
                                                    "\t(3) REPORTS\n"
                                                    "\t(4) LOGOUT\n" +
              "_" * 80)

    def display_manager_homepage(self):
        #Displays the homepage if the user is of manager user type
        print("*" * 36 + " HOME PAGE " + "*" * 36 + "\n"  # Order Main Menu
                                                    "\t(1) ORDER MENU\n"
                                                    "\t(2) INVENTORY\n"
                                                    "\t(3) LOGOUT\n" +
              "_" * 80)

    def display_homepage(self):
        # Displays the homepage if the user is of staff user type
        print("*" * 36 + " HOME PAGE " + "*" * 36 + "\n"  # Order Main Menu
                                                    "\t(1) ORDER MENU\n"
                                                    "\t(2) LOGOUT\n" +
              "_" * 80)
    def display_order_main(self):
        #Displays the main menu of orders
        print("*" * 41 + "*" * 41 + "\n")
        print(" " * 30 + " OLIVER'S BAKESHOP " + " " * 30 + "\n")
        print("*" * 41 + "*" * 41 + "\n")
        print("*" * 36 + " ORDER PAGE " + "*" * 36 + "\n"  # Order Main Menu
                                                     "\t(1) CREATE ORDER\n"
                                                     "\t(2) MAIN MENU\n"
        +
              "_" * 80)

    def display_report_menu(self):
        #Displays the main menu of reports
        print("*" * 36 + " REPORTS PAGE " + "*" * 36 + "\n"  # Report Main Menu
                                                       "\t(1) Low in inventory at the end of each week in each store\n"
                                                       "\t(2) Total number of coffee sold in last month in each store\n"
                                                       "\t(3) Total number of coffee beans (in quantity) sold in last month in each store\n"
                                                       "\t(4) Total number of food items sold in last month in each store\n"
                                                       "\t(5) Type of coffee sold the most per store in the last month\n"
                                                       "\t(6) Days of the week that made the most sale in the last month per store\n"
                                                       "\t(7) Total sale made in dollars in the last month per store\n"
                                                       "\t(8) HOMEPAGE\n"

              +
              "_" * 80)

    def display_inventory_menu(self):
        # Displays the main menu of inventory
        print("*" * 36 + " INVENTORY PAGE " + "*" * 36 + "\n"  # Report Main Menu
                                                       "\t(1) ADD INVENTORY\n"
                                                       "\t(2) HOMEPAGE\n"
              +
              "_" * 80)

