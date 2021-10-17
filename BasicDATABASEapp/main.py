from tkinter import *
import memberSearch
import addMembers
import checkIn
import checkOut
import calculatePay
from PIL import ImageTk, Image

root = Tk()


def open_member_search():
    top = Toplevel()
    layer = memberSearch.SearchMember(top)
    # idk why it says its never being used


def open_member_add():
    top = Toplevel()
    layer = addMembers.AddMember(top)
    # idk why it says its never being used


def open_check_in():
    top = Toplevel()
    layer = checkIn.CheckinMember(top)


def open_check_out():
    top = Toplevel()
    layer = checkOut.CheckOutMember(top)


def open_calculate_pay():
    top = Toplevel()
    layer = calculatePay.MemberPay(top)


class Home:
    def __init__(self, master):
        # my_frame = Frame(master)
        # my_frame.grid()

        # declare widgets & labels
        self.header_label = Label(master, text="Record Manager V = 2.0", padx=100)

        self.add_member_button = Button(master, text="Add Employee", padx=40, width=20, command=open_member_add)
        self.search_member_button = Button(master, text="Search Employee", padx=40, width=20, command=open_member_search)
        self.check_in_button = Button(master, text="Check In", padx=40,width=20, command=open_check_in)

        self.check_out_button = Button(master, text="Check Out", padx=40, width=20,command=open_check_out)
        self.calculate_pay_button = Button(master, text="Payment Calc", padx=40, width=20,command=open_calculate_pay)
        self.server_status = Button(master, text="Server Status", padx=40, width=20, command=open_calculate_pay)

        self.image_one = ImageTk.PhotoImage(Image.open("PM logo.png"))
        self.image_label_one = Label(master, image=self.image_one)

        # grid widgets & labels
        self.header_label.grid(row=0, column=0, columnspan=6)

        self.add_member_button.grid(row=1, column=0, columnspan=1)
        self.search_member_button.grid(row=1, column=1, columnspan=1)
        self.check_in_button.grid(row=1, column=2, columnspan=1)

        self.check_out_button.grid(row=2, column=0, columnspan=1)
        self.calculate_pay_button.grid(row=2, column=1, columnspan=1)
        self.server_status.grid(row=2, column=2, columnspan=1)

        self.image_label_one.grid(row=3, column=0, columnspan=6)


# root.configure(bg='black')
icon = PhotoImage(file="PM logo.png")
root.title("Payments Manager")
root.iconphoto(False, icon)


app = Home(root)
mainloop()
