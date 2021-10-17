from tkinter import *
import mysql.connector
import StringChecker as SC


class SearchMember:

    def search_request(self):
        query = "SELECT * FROM employees WHERE first_name = %s AND last_name = %s"
        text = ""

        # checking the string for sql injection
        if not SC.check_string(self.search_box.get()):
            return

        try:
            entry = (self.search_box.get()).split(" ")
            data = (entry[0], entry[1])
            self.sql_cursor.execute(query, data)
            count = 0
            # concatenating the label text with the fetched cursor result
            for x in self.sql_cursor:
                text = text + str(x)
                text = text + "\n"
                count += 1
                if count > 10:
                    break

            self.search_table["text"] = text
        except IndexError:
            self.search_table["text"] = "no result"

    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.grid()

        # sql connector
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="17MM3102",
            database="PayRollDB",
            auth_plugin='mysql_native_password'
            )

        # database cursor
        self.sql_cursor = self.db.cursor()

        # variables

        # declare widgets & labels
        self.header_label = Label(master, text="Search employee details", padx=100)
        self.search_box = Entry(master, width=80)
        self.search_button = Button(master, text="search", padx=20, command=lambda: self.search_request())
        self.search_table = Label(master, text="", padx=100)

        # grid widgets & labels
        self.header_label.grid(row=0, column=0, columnspan=6)
        self.search_button.grid(row=1, column=5, columnspan=1)
        self.search_box.grid(row=1, column=0, columnspan=1)
        self.search_table.grid(row=2, column=0, columnspan=4)
