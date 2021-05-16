'''
--------------------FIT5136_SEM_02_Team 09  Assignment 4B - Bakeshop System -------------------------------
Author Names & IDs : Dipal Vyas(31847390) , Aashna Jain(29802911) , Nivedha Balasubramanian(30729963), Kanika Bansal(31030319)
Start Date : 16th September, 2020
End Date : 1st November, 2020
------------------------------------------------------------------------------------------------------------
Class Description: Report class is used to get reports from bakeshop data and present it to the viewer.
------------------------------------------------------------------------------------------------------------
'''
from BakeshopData import BakeshopData
# This class is used to generate reports according to the prompt given by user
class Report:
    # init constructor is used to generate the report
    def __init__(self):
        self.bakeshop_data = BakeshopData()

    # Get total number of coffee beans sold in last month
    def get_total_coffee_beans_sold(self):
        bakeshop_data = BakeshopData()
        bakeshop_data.generate_coffee_bean_report()

    # Get total number of food items sold in last month
    def get_total_number_of_items(self):
        bakeshop_data = BakeshopData()
        bakeshop_data.generate_total_food_sold()

    # Get total number of coffee sold in last month
    def get_total_number_of_coffee(self):
        bakeshop_data = BakeshopData()
        bakeshop_data.generate_total_coffee_sold()

    # Get coffee type the most sold in last month
    def get_coffe_type_sold(self):
        bakeshop_data = BakeshopData()
        bakeshop_data.generate_coffee_type_sold()

    # Get the days of the week that made the most sale in last month
    def get_days_of_week_most_sale(self):
        bakeshop_data = BakeshopData()
        bakeshop_data.generate_days_of_week_report()

    # Get the items which are low in inventory
    def get_low_in_inventory(self):
        self.bakeshop_data.generate_low_in_inventory_report()

    # Get total sale made in a month
    def get_sale_made_in_month(self):
        self.bakeshop_data.generate_sale_made_in_month()