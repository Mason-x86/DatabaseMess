from tkinter import *
import mysql.connector
from datetime import date
# , datetime, timedelta
import StringChecker as SC


class AddMember:

    def add_request(self):
        # check the user strings for dangerous inputs
        if not SC.check_string(self.first_name_box.get()):
            return
        elif not SC.check_string(self.surname_box.get()):
            return
        elif not SC.check_string(self.date_box.get()):
            return

        # Adds a employee to the database with sql connector
        # splits date time string into 3 integers for date type declaring
        first_name = self.first_name_box.get()
        last_name = self.surname_box.get()
        date_str = (self.date_box.get()).split(":")
        gender = self.gender_box.get()
        try:
            # declaring the date type with split ints
            date_hired = date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
            insert_stmt = (
                "INSERT INTO employees (first_name, last_name, gender, date_hired)"
                "VALUES (%s, %s, %s, %s)"
            )
            data = (first_name, last_name, gender, date_hired)
            self.sql_cursor.execute(insert_stmt, data)
            self.db.commit()
            self.error_box["text"] = "add complete!"
        except ValueError:
            # if the client types a invalid date that cannot convert to string
            self.error_box["text"] = "error invalid inputs!"

    def __init__(self, master):
        # sql connector
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="????????",
            database="PayRollDB",
            auth_plugin='mysql_native_password'
            )

        # database cursor
        self.sql_cursor = self.db.cursor()

        # declare widgets & labels
        self.header_label = Label(master, text="Add Employee", padx=100)
        self.first_name_box = Entry(master, width=80)
        self.surname_box = Entry(master, width=80)
        self.gender_box = Entry(master, width=80)
        self.date_box = Entry(master, width=80)
        self.first_name_label = Label(master, text="First Name", padx=40)
        self.surname_label = Label(master, text="Surname", padx=40)
        self.gender_label = Label(master, text="Gender", padx=40)
        self.date_label = Label(master, text="Date(yr:mt:dy)", padx=40)
        self.add_button = Button(master, text="Add", padx=20, command=lambda: self.add_request())
        self.error_box = Label(master, text="", padx=40)

        # grid widgets & labels
        self.header_label.grid(row=0, column=0, columnspan=6)
        self.add_button.grid(row=5, column=6, columnspan=1)

        self.first_name_box.grid(row=1, column=0, columnspan=1)
        self.first_name_label.grid(row=1, column=6, columnspan=1)

        self.surname_box.grid(row=2, column=0, columnspan=1)
        self.surname_label.grid(row=2, column=6, columnspan=1)

        self.gender_box.grid(row=3, column=0, columnspan=1)
        self.gender_label.grid(row=3, column=6, columnspan=1)

        self.date_box.grid(row=4, column=0, columnspan=1)
        self.date_label.grid(row=4, column=6, columnspan=1)

        self.error_box.grid(row=5, column=0, columnspan=1)
