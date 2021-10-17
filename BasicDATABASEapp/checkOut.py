from tkinter import *
import mysql.connector
from datetime import date, timedelta
import StringChecker as SC


class CheckOutMember:

    # bridges the employee id with the checkin id with a middle man table
    def bridge_check_out_request(self, check_in_date):
        try:
            select_stmt = (
                "SELECT Check_ID FROM check_Out "
                "WHERE check_Out_date = %s"
            )
            data = (str(check_in_date), )
            self.sql_cursor.execute(select_stmt, data)
            checkin_id = self.sql_cursor.fetchone()

            insert_stmt = (
                "INSERT INTO Employee_Check_Out_Bridge (Check_ID, Employ_ID)"
                "VALUES (%s, %s)"
            )
            self.error_box["text"] = self.employ_id_box.get(), checkin_id
            idn = int(checkin_id["Check_ID"])  # I did this to check for type error
            data = (idn, self.employ_id_box.get())
            self.sql_cursor.execute(insert_stmt, data)
            self.db.commit()

        except ValueError:
            self.error_box["text"] += " ValueError"

    def check_out_request(self):
        # check the string for dangerous characters
        if not SC.check_string(self.date_box.get()):
            return
        elif not SC.check_string(self.time_box.get()):
            return

        # Adds an employee to the database with sql connector
        # splits date time string into 3 integers for date type declaring
        date_str = (self.date_box.get()).split(":")
        time_str = (self.time_box.get()).split(":")
        try:
            # using the list of ints I declare date/ time variables
            date_stamped = date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
            time_stamped = timedelta(int(time_str[0]), int(time_str[1]), 7)
            # this statement fills a new checkin member with the date/time giving a auto id
            insert_stmt = (
                "INSERT INTO check_Out(check_Out_date, check_Out_time)"
                "VALUES (%s, %s)"
            )
            data = (date_stamped, time_stamped)
            self.sql_cursor.execute(insert_stmt, data)
            self.db.commit()
            self.error_box["text"] = "add complete!"
            self.bridge_check_out_request(date_stamped)

        except ValueError:
            self.error_box["text"] = "error invalid inputs! checkin request"

    def __init__(self, master):
        # sql connector
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="???????",
            database="PayRollDB",
            auth_plugin='mysql_native_password'
            )

        # database cursor
        self.sql_cursor = self.db.cursor(buffered=True, dictionary=True)

        # declare widgets & labels
        self.employ_id_box = Entry(master, width=80)
        self.date_box = Entry(master, width=80)
        self.time_box = Entry(master, width=80)
        self.employ_id_label = Label(master, text="Employee ID", padx=40)
        self.date_label = Label(master, text="check out time (yr:mt:dy)", padx=40)
        self.time_label = Label(master, text="check out time (hr:mn)", padx=40)
        self.add_button = Button(master, text="Add", padx=20, command=lambda: self.check_out_request())
        self.error_box = Label(master, text="", padx=40)

        # grid widgets & labels
        self.add_button.grid(row=5, column=6, columnspan=1)

        self.employ_id_box.grid(row=1, column=0, columnspan=1)
        self.employ_id_label.grid(row=1, column=6, columnspan=1)

        self.date_box.grid(row=2, column=0, columnspan=1)
        self.date_label.grid(row=2, column=6, columnspan=1)

        self.time_box.grid(row=3, column=0, columnspan=1)
        self.time_label.grid(row=3, column=6, columnspan=1)

        self.error_box.grid(row=5, column=0, columnspan=1)
