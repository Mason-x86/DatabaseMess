from tkinter import *
import mysql.connector
import StringChecker as SC


class MemberPay:

    def calc_request(self):
        # checking the string for sql injection
        if not SC.check_string(self.search_box.get()):
            return

        # get id --> get times --> calc difference
        query = "SELECT Check_ID FROM Employee_Check_In_Bridge WHERE Employ_ID = %s"
        data = [self.search_box.get(), ]
        self.sql_cursor.execute(query, data)
        check_in_id = self.sql_cursor.fetchone()
        try:
            query = "SELECT check_In_time, check_In_date FROM check_In WHERE check_iD = %s"
            data = [check_in_id[0], ]
            self.sql_cursor.execute(query, data)
            in_times = self.sql_cursor.fetchall()
        except TypeError:
            return

        query = "SELECT Check_ID FROM Employee_Check_Out_Bridge WHERE Employ_ID = %s"
        data = [self.search_box.get(), ]
        self.sql_cursor.execute(query, data)
        check_out_id = self.sql_cursor.fetchone()
        try:
            query = "SELECT check_Out_time, check_Out_date FROM check_Out WHERE check_iD = %s"
            data = [check_out_id[0], ]
            self.sql_cursor.execute(query, data)
            out_times = self.sql_cursor.fetchall()
        except TypeError:
            return

    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.grid()

        # sql connector
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="???????",
            database="PayRollDB",
            auth_plugin='mysql_native_password'
        )

        # database cursor
        self.sql_cursor = self.db.cursor()

        # variables

        # declare widgets & labels
        self.header_label = Label(master, text="Enter employee number", padx=100)
        self.search_box = Entry(master, width=80)
        self.search_button = Button(master, text="Calculate", padx=20, command=lambda: self.calc_request())
        self.search_table = Label(master, text="", padx=100)

        # grid widgets & labels
        self.header_label.grid(row=0, column=0, columnspan=6)
        self.search_button.grid(row=1, column=5, columnspan=1)
        self.search_box.grid(row=1, column=0, columnspan=1)
        self.search_table.grid(row=2, column=0, columnspan=4)
