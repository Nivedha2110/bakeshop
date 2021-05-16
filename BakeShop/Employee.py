'''
--------------------FIT5136_SEM_02_Team 09  Assignment 4B - Bakeshop System -------------------------------
Author Names & IDs : Dipal Vyas(31847390) , Aashna Jain(29802911) , Nivedha Balasubramanian(30729963), Kanika Bansal(31030319)
Start Date : 16th September, 2020
End Date : 1st November, 2020
------------------------------------------------------------------------------------------------------------
Class Description: Employee class stores the employee details and retrieves it when needed
------------------------------------------------------------------------------------------------------------
'''

import os
import pandas as pd

class Employee:
    # Retrieve employee id from user email address
    def get_emp_id(self, user):
        df = self.read_from_excel()
        if (df['email'].isin([user]).any().any()):
            temp = df.loc[df['email'] == user, ['employee Id']].to_string()
            password = temp.split()
            return password[3]
        else:
            return ""

    # Retrieve employee name from user email address
    def get_emp_name(self, user):
        df = self.read_from_excel()
        if (df['email'].isin([user]).any().any()):
            temp = df.loc[df['email'] == user, ['employee name']].to_string()
            name = temp.split()
            return name[3]
        else:
            return ""

    # Retrieve employee email from user email address
    def get_emp_email(self, user):
        df = self.read_from_excel()
        if df['email'].isin([user]).any().any():
            temp = df.loc[df['email'] == user, ['email']].to_string()
            email = temp.split()
            return email[2]
        else:
            return ""

    # Retrieve employee store id from user email address
    def get_emp_store_id(self, username):
        df = self.read_from_excel()
        if (df['email'].isin([username]).any().any()):
            temp = df.loc[df['email'] == username, ['store id']].to_string()
            str_id = temp.split()
            store_id = str_id[3]
            # If employee has multiple store prompt him to select only 1 store for 1 function
            if '|' in store_id:
                store_id_list = store_id.split(sep='|')
                while (True):
                    try:
                        print("You have access to multiple stores")
                        i = 1
                        for x in store_id_list:
                            print(str(i) + ": " + "Store ID " + str(x))
                            i = i + 1
                        store = int(input("Please choose the option number for the store ID for this order: "))

                        if store in range(1, len(store_id_list) + 1):
                            store_id = store
                            return store_id
                        else:
                            print("Invalid choice of store")

                    except ValueError:
                        print("Invalid Input! Please Try Again.")
                        print("\n" * 1)

            return store_id
        else:
            return ""

    # Retrieve employee user type from user email address
    def get_emp_user_type(self, user):
        df = self.read_from_excel()
        if df['email'].eq(user).any():
            temp = df.loc[df['email'] == user, ['User Type']].to_string()
            user_type = temp.split()
            return user_type[3]
        else:
            return ""

    # Retrieve employee password from user email address
    def get_emp_password(self, username):
        df = self.read_from_excel()
        if df['email'].eq(username).any():
            temp = df.loc[df['email'] == username, ['password']].to_string()
            password = temp.split()
            return password[2]
        else:
            return ""

    # Read the values in employee database
    def read_from_excel(self):
        path = os.getcwd().replace("\\", "/")
        data = pd.read_excel(path + '/SampleData.xlsx', sheet_name='users')
        df = pd.DataFrame(data)
        return df
