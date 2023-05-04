from Menu import *
from PyQt5.QtWidgets import *


class Controller(QMainWindow, Ui_LabMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.SHOPButton.clicked.connect(lambda: self.shop())
        self.ExitButton.clicked.connect(lambda: self.exit())
        #add the other 6 button
        self.Add_cookie.clicked.connect(lambda: self.cookie_add())
        self.Add_water.clicked.connect(lambda: self.water_add())
        self.Add_sandwich.clicked.connect(lambda: self.sandwich_add())
        self.Remove_cookie.clicked.connect(lambda: self.cookie_remove())
        self.Remove_water.clicked.connect(lambda: self.water_remove())
        self.Remove_sandwich.clicked.connect(lambda: self.sandwich_remove())

        self.menulabel.setText(f"               Welcome \n\n\n              Customers!")

        self.SHOPButton.setHidden(False)
        self.ExitButton.setHidden(True)
        self.Add_cookie.setHidden(True)
        self.Add_water.setHidden(True)
        self.Add_sandwich.setHidden(True)
        self.Remove_cookie.setHidden(True)
        self.Remove_water.setHidden(True)
        self.Remove_sandwich.setHidden(True)
        self.lineEditCookie.setHidden(True)
        self.lineEditSandwich.setHidden(True)
        self.lineEditWater.setHidden(True)

        self.cookie = float(1.50)
        self.sandwich = float(4.00)
        self.water = float(1.00)
        self.customer_total = float(0.00)
        "Add an input for Quantity"

        # self.ck = int(self.lineEditCookie.text())
        # self.Int_cookie = self.ck
        # self.cookie_amount = 0
        # self.sandwich_amount = 0
        # self.water_amount = 0
        self.tax = float(0.10)
        self.total_tax = float(0)
    def menu(self):
        self.menulabel.setText(f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")
        self.Add_cookie.setHidden(False)
        self.Add_water.setHidden(False)
        self.Add_sandwich.setHidden(False)
        self.Remove_cookie.setHidden(False)
        self.Remove_water.setHidden(False)
        self.Remove_sandwich.setHidden(False)
        self.lineEditCookie.setHidden(False)
        self.lineEditSandwich.setHidden(False)
        self.lineEditWater.setHidden(False)

        self.lineEditCookie.setText("0")
        self.lineEditSandwich.setText("0")
        self.lineEditWater.setText("0")


    def cookie_add(self):
        '''everytime button is pressed add cookie'''
        # self.cookie_amount += 1
        #converted text to int
        try:
            ck = int(self.lineEditCookie.text())
            self.lineEditCookie.setText(f"{ck + 1}")
        except ValueError:
            self.lineEditCookie.setText(f"Invalid")
            self.lineEditCookie.setText("0")
        # self.menulabel.setText(f"\n\n--Lah's Bakery Menu--\n\n{ck * 2}     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")

    def water_add(self):
        '''everytime button is pressed add water'''
        # wt = int(self.lineEditWater.text('0'))
        # self.lineEditWater.setText(f"{wt + 1}")
        # self.water_amount += 1
        # self.menulabel.setText(f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")

    def sandwich_add(self):
        '''everytime button is pressed add sandwich'''
        self.sandwich_amount += 1
        self.menulabel.setText(f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")


    def cookie_remove(self):
        '''everytime button is pressed remove cookie'''
        if self.cookie_amount <= 0:
            self.cookie_amount -= 0
        else:
            self.cookie_amount -= 1
            self.menulabel.setText(
                f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")

    def water_remove(self):
        '''everytime button is pressed remove water'''
        if self.water_amount <= 0:
            self.water_amount -= 0
        else:
            self.water_amount -= 1
            self.menulabel.setText(
                f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")

    def sandwich_remove(self):
        '''everytime button is pressed remove sandwich'''
        if self.sandwich_amount <= 0:
            self.sandwich_amount -= 0
        else:
            self.sandwich_amount -= 1
            self.menulabel.setText(
                f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")

    def shop(self):
        self.menu()
        self.SHOPButton.setHidden(True)
        self.ExitButton.setHidden(False)

    def receipt(self):
        self.customer_total = (self.cookie_amount * self.cookie) + (self.sandwich_amount * self.sandwich) + (
                    self.water_amount * self.water)
        self.total_tax = self.customer_total * self.tax
        # self.ReceiptLabel.setText(
        #     f"\t\t\tReceipt\n\t\t({self.cookie_amount})Cookie......................${self.cookie_amount * self.cookie:.2f}\n"
        #     f"\t\t({self.sandwich_amount})Sandwich......................${self.sandwich_amount * self.sandwich:.2f}\n"
        #     f"\t\t({self.water_amount})Water......................${self.water_amount * self.water:.2f}\n\n\n"
        #     f"\t\tTax 10%..........................${self.total_tax:.2f}\n"
        #     f"\t\tTotal Amount................${self.customer_total + self.total_tax:.2f}")

        self.lineEditCookie.setHidden(True)
        self.lineEditSandwich.setHidden(True)
        self.lineEditWater.setHidden(True)

    def exit(self):
        '''add up the total cost and label everything'''
        self.Add_cookie.setHidden(True)
        self.Add_water.setHidden(True)
        self.Add_sandwich.setHidden(True)
        self.Remove_cookie.setHidden(True)
        self.Remove_water.setHidden(True)
        self.Remove_sandwich.setHidden(True)
        self.menulabel.clear()
        self.ExitButton.setHidden(True)
        self.receipt()
