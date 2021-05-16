####################################################
# Importing all the libraries and classes needed
####################################################

import pandas as pd
from Item import Item
import os
from datetime import datetime
from Order import Order
import calendar
import openpyxl

class BakeshopData:

    ###############################################################################
    # Total Number of Coffee Beans Quantity Sold in the Last Month in Each Store.
    ###############################################################################
    def generate_coffee_bean_report(self):
        # Initialising order class and calling the read_from_excel function from it.
        order = Order()
        df = order.read_from_excel()
        count_item = dict()  # Empty Dictionary

        for i in range(len(df)):  # iterating over the dataframe
            # getting month from the date extracted
            datee = str(df.iloc[i, 7]).split("/")
            month = datee[0]

            x = datetime.now()  # getting the date and time of the present
            current_month = x.strftime("%m")  # stripping the month from it
            prev_month = datetime.strptime(str(int(current_month) - 1), "%m")
            if int(month) == (int(int(current_month) - 1)) and int(datee[2]) == int(x.strftime("%Y")):
                item_name = "roast coffee beans "
                item = df.iloc[i, 3]
                if item == item_name:
                    quantity = df.iloc[i, 4]
                    store_id = df.iloc[i, 0]

                    # Checking if store id is in the dictionary then appending the quantity to store id
                    if store_id in count_item:
                        count_item[store_id] = int(count_item[store_id]) + int(quantity)
                    else:
                        count_item[store_id] = quantity

        print("The store IDs that are not mentioned below do not have any coffee bean sold in the month of " + str(
            prev_month.strftime("%B")))
        print("\n")
        for x, y in sorted(count_item.items()):
            print("Store ID: " + str(x))
            print("Item Name : " + item_name)
            print(
                "Total Coffee Beans(Quantity) sold for the month of " + str(prev_month.strftime("%B")) + " is: " + str(
                    y))
            print("\n")

    ###########################################################################################
    # Total Number of Food Items Sold in Last Month in Each Store  
    ###########################################################################################

    def generate_total_food_sold(self):
        # Initialising order class and calling the read_from_excel function from it.
        order = Order()
        df = order.read_from_excel()
        categories = ['Bread', 'Dessert', 'Sandwich', 'Cake', 'Burger']  # Categories for food items
        item_obj = Item()
        store_list = []
        item_list = []
        quantity_list = []

        for i in range(len(df)):
            # getting month from the date extracted
            datee = str(df.iloc[i, 7]).split("/")
            month = datee[0]
            x = datetime.now()
            current_month = x.strftime("%m")

            if int(month) == (int(int(current_month) - 1)) and int(datee[2]) == int(x.strftime("%Y")):

                item = df.iloc[i, 3]
                if ',' in item:
                    item = item.split(sep=',')  # Splitting the items
                    k = -1
                    quantity = df.iloc[i, 4].split(', ')  # Splitting the quantities of each item
                    for x in item:
                        k = k + 1
                        a = x.strip()
                        cat = item_obj.get_item_category(a)
                        # Getting items according to categories and appending them to item_list and their quantity to quantity_list
                        if cat in categories:
                            store_item = df.iloc[i, 0]
                            store_list.append(store_item)
                            item_list.append(a)
                            quantity_list.append(int(quantity[k]))

                else:
                    quantity = df.iloc[i, 4]
                    a = item.strip()
                    if a == "roast coffee beans":
                        continue
                    cat = item_obj.get_item_category(a)
                    if cat in categories:
                        store_item = df.iloc[i, 0]
                        store_list.append(store_item)
                        item_list.append(a)
                        quantity_list.append(int(quantity[k]))

        report = dict()
        for i in range(len(store_list)):
            if store_list[i] not in report:
                report[store_list[i]] = {}
                # Appending items and quantities to the dictionary according to store
            if item_list[i] in report[store_list[i]]:
                report[store_list[i]][item_list[i]] += quantity_list[i]
            else:
                report[store_list[i]][item_list[i]] = quantity_list[i]

        prev_month = datetime.strptime(str(int(current_month) - 1), "%m")

        print("The store IDs that are not mentioned below do not have any food item sold in the month of " + str(
            prev_month.strftime("%B")))
        print("\n")

        for x, y in report.items():
            print("Store ID: " + str(x))
            quantity = 0
            for a, b in y.items():
                print("Item name: " + a)
                print("Item quantity: " + str(b))
                quantity += b

            print("Total items sold for the month of " + str(prev_month.strftime("%B")) + " is: " + str(quantity))
            print("\n")

    ########################################################################################## 
    # Days of the Week That Made the Most Sale in the Last Month per Store  
    ##########################################################################################

    def generate_days_of_week_report(self):
        order = Order()
        df = order.read_from_excel()
        date_list = []
        store_list = []
        sale_list = []
        weekday_list = []
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for i in range(len(df)):
            # getting month from the date extracted
            datee = str(df.iloc[i, 7]).split("/")
            month = datee[0]
            x = datetime.now()
            current_month = x.strftime("%m")
            if int(month) == (int(int(current_month) - 1)) and int(datee[2]) == int(x.strftime("%Y")):
                weekday = datetime(int(datee[2]), int(datee[0]), int(datee[1])).strftime('%A')
                print(weekday)
                total_sales = df.iloc[i, 6]
                store_id = df.iloc[i, 0]
                date_list.append(datee)  # Adding the dates to the list
                weekday_list.append(weekday)
                store_list.append(store_id)  # Appending the stores to the list
                sale_list.append(float(total_sales))

        report = dict()
        for i in range(len(store_list)):
            if store_list[i] not in report:
                report[store_list[i]] = [0, 0, 0, 0, 0, 0, 0]

            for j in range(7):
                # Checking for a week if the weekday is equal to days then adding sale of that day according to store
                if weekday_list[i] == days[j]:
                    report[store_list[i]][j] = report[store_list[i]][j] + sale_list[i]

        prev_month = datetime.strptime(str(int(current_month) - 1), "%m")

        print("The store IDs that are not mentioned below do not have any item sold in the month of " + str(
            prev_month.strftime("%B")))
        print("\n")

        for x, y in report.items():
            quantity = 0
            pos = 0
            for i in range(7):
                if y[i] > quantity:
                    quantity = y[i]
                    pos = i
            print("Store ID: " + str(x))
            print("The day with the most sale is: " + str(days[pos]))
            print("Total quantity sold in the month of " + str(prev_month.strftime("%B")) + ": " + str(quantity))
            print("\n")

    ##########################################################################################
    # Total Number of Coffee Sold in the Last Month in Each Store  
    ##########################################################################################

    def generate_total_coffee_sold(self):
        # Initialising order class and calling the read_from_excel function from it.
        order = Order()
        df = order.read_from_excel()
        categories = ['Coffee']
        item_obj = Item()
        store_list = []
        item_list = []
        quantity_list = []
        for i in range(len(df)):
            # getting month from the date extracted
            datee = str(df.iloc[i, 7]).split("/")
            month = datee[0]
            x = datetime.now()
            current_month = x.strftime("%m")
            if int(month) == (int(int(current_month) - 1)) and int(datee[2]) == int(x.strftime("%Y")):
                item = df.iloc[i, 3]
                if ',' in item:
                    item = item.split(sep=',')  # Splitting the items
                    k = -1
                    quantity = df.iloc[i, 4].split(', ')
                    for x in item:
                        k = k + 1
                        a = x.strip()
                        cat = item_obj.get_item_category(a)
                        if cat in categories:
                            store_item = df.iloc[i, 0]
                            store_list.append(store_item)
                            item_list.append(a)
                            quantity_list.append(int(quantity[k]))
        report = dict()
        for i in range(len(store_list)):
            if store_list[i] not in report:
                report[store_list[i]] = {}
                # Appending items and quantities to the dictionary according to store
            if item_list[i] in report[store_list[i]]:
                report[store_list[i]][item_list[i]] += quantity_list[i]
            else:
                report[store_list[i]][item_list[i]] = quantity_list[i]
        prev_month = datetime.strptime(str(int(current_month) - 1), "%m")

        print("The store IDs that are not mentioned below do not have any coffee items sold in the month of " + str(
            prev_month.strftime("%B")))
        print("\n")

        for x, y in report.items():
            print("Store ID: " + str(x))
            quantity = 0
            for a, b in y.items():
                print("Item name: " + a)
                print("Item quantity: " + str(b))
                quantity += b
            print("Total items sold for the month of " + str(prev_month.strftime("%B")) + " is: " + str(quantity))
            print("\n")

    ##########################################################################################  
    # Type of Coffee Sold the Most per Store in the Last Month  
    ##########################################################################################
    def generate_coffee_type_sold(self):
        order = Order()
        df = order.read_from_excel()
        categories = ['Coffee']
        item_obj = Item()
        store_list = []
        item_list = []
        quantity_list = []
        for i in range(len(df)):
            # getting month from the date extracted
            datee = str(df.iloc[i, 7]).split("/")
            month = datee[0]
            x = datetime.now()
            current_month = x.strftime("%m")
            if int(month) == (int(int(current_month) - 1)) and int(datee[2]) == int(x.strftime("%Y")):

                item = df.iloc[i, 3]
                if ',' in item:
                    item = item.split(sep=',')
                    k = -1
                    quantity = df.iloc[i, 4].split(', ')
                    for x in item:
                        k = k + 1
                        a = x.strip()
                        cat = item_obj.get_item_category(a)
                        # Getting items according to categories and appending them to item_list and their quantity to quantity_list
                        if cat in categories:
                            store_item = df.iloc[i, 0]
                            store_list.append(store_item)
                            item_list.append(a)
                            quantity_list.append(int(quantity[k]))
        report = dict()

        for i in range(len(store_list)):
            report[store_list[i]] = []
        for i in range(len(store_list)):
            if report[store_list[i]] != []:
                current_quantity = int(report[store_list[i]][0][1])
                if current_quantity < quantity_list[i]:
                    report[store_list[i]] = [[item_list[i], quantity_list[i]]]
            else:
                report[store_list[i]].append([item_list[i], quantity_list[i]])

        prev_month = datetime.strptime(str(int(current_month) - 1), "%m")

        print("The store IDs that are not mentioned below do not have any coffee item sold in the month of " + str(
            prev_month.strftime("%B")))
        print("\n")

        for x, y in report.items():
            print("Store ID: " + str(x))
            quantity = 0
            for i in range(len(y)):
                print("Item name: " + str(y[i][0]))
                print("Item quantity: " + str(y[i][1]))
                quantity += int(y[i][1])
            print("Total coffee type most sold for the month of " + str(prev_month.strftime("%B")) + " is: " + str(
                quantity))
            print("\n")

    # def get_inventory_data(self):
    #     path = os.getcwd().replace("\\", "/")
    #     data = pd.read_excel(path + '/SampleData.xlsx', sheet_name='Item')
    #     df = pd.DataFrame(data)
    #     return df

    ##########################################################################################
    # Low in Inventory at the End of Each Week in Each Store
    ##########################################################################################
    def generate_low_in_inventory_report(self):
        date_time = datetime.now()
        saturday_flag = datetime.weekday(date_time)
        path = os.getcwd().replace("\\", "/")
        file = path + '/SampleData.xlsx'
        wb = openpyxl.load_workbook(filename=file)
        ws = wb['Last_Low_Inventory']
        if saturday_flag == 5:
            data = self.get_inventory_data()
            filter_data = data[data['quantity'] <= 5]
            selected_columns = filter_data[['store id', 'Item Name', 'quantity']]
            selected_columns_to_store = filter_data[['store id', 'Item Name', 'quantity']].values.tolist()
            selected_columns = selected_columns.groupby(['store id'])
            for key, item in selected_columns:
                print((selected_columns.get_group(key)).to_string(index=False), "\n\n")
            row = 2
            for i in selected_columns_to_store:
                row1 = [i[0], i[1], i[2]]
                for col, entry in enumerate(row1, start=1):
                    ws.cell(row=row, column=col, value=entry)

                wb.save(file)
                row = row + 1
        else:
            path = os.getcwd().replace("\\", "/")
            data = pd.read_excel(path + '/SampleData.xlsx', sheet_name='Last_Low_Inventory')
            df = pd.DataFrame(data)
            df = df.groupby(['Store ID'])
            for name, group in df:
                print(group.to_string(index=False))

    ########################################################################################## 
    # Total Sale Made in Dollars in the Last Month per Store 
    ##########################################################################################

    def generate_sale_made_in_month(self):
        date_time = datetime.now()
        date = date_time.strftime("%m/%d/%Y")
        path = os.getcwd().replace("\\", "/")
        data = pd.read_excel(path + '/SampleData.xlsx', sheet_name='orders')
        df = pd.DataFrame(data)
        end_date = calendar.monthrange(date_time.year, int(date_time.month) - 1)[1]
        month = int(date_time.month) - 1
        month_name = calendar.month_name[month]
        if len(str(month)) == 1:
            month = '0' + str(month)
        last_month = month + '/01/' + str(date_time.year)
        current_month = month + '/' + str(end_date) + '/' + str(date_time.year)
        filter_data = df[(df['date '] >= str(last_month)) & (df['date '] <= str(current_month))]
        filter_data = filter_data[['store id', 'total amount']]
        filter_data = filter_data.groupby(['store id'])['total amount'].sum().reset_index()
        # filter_data = filter_data.groupby(['store id'])
        print("Total Sales in the last month - " + month_name)
        # grouped_df = df.groupby('A')

        # for key, item in filter_data:
        #     print(filter_data.get_group(key),item , "\n\n")

        print(filter_data.to_string(index=False))


if __name__ == "__main__":
    bd = BakeshopData()
    bd.generate_total_food_sold()