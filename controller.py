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
        self.Remove_sandwich.clicked.connect(lambda: self.water_remove())

        self.menulabel.setText(f"               Welcome \n\n\n              Customers!")

        self.SHOPButton.setHidden(False)
        self.ExitButton.setHidden(True)
        self.Add_cookie.setHidden(True)
        self.Add_water.setHidden(True)
        self.Add_sandwich.setHidden(True)
        self.Remove_cookie.setHidden(True)
        self.Remove_water.setHidden(True)
        self.Remove_sandwich.setHidden(True)

        self.cookie = 0.00
        self.sandwich = 0.00
        self.water = 0.00
        self.customer_total = 0.00
        self.cookie_amount = 0.00
        self.sandwich_amount = 0.00
        self.water_amount = 0.00

    def menu(self):
        self.menulabel.setText(f"\n\n--CART MENU--\n\n ({self.cookie_amount})Cookie - $1.50\n ({self.sandwich_amount})Sandwich - $4.00\n ({self.water_amount})Water - $1.00")
        self.Add_cookie.setHidden(False)
        self.Add_water.setHidden(False)
        self.Add_sandwich.setHidden(False)
        self.Remove_cookie.setHidden(False)
        self.Remove_water.setHidden(False)
        self.Remove_sandwich.setHidden(False)
    # cookie = 0.00
    # sandwich = 0.00
    # water = 0.00
    # customer_total = 0.00
    # cookie_amount = 0
    # sandwich_amount = 0
    # water_amount = 0

    def cookie_add(self):
        '''everytime button is pressed add cookie'''
        self.cookie_amount += 1.5
        self.customer_total += 1.5



    def water_add(self):
        '''everytime button is pressed add water'''
        self.water_amount += 1
        self.customer_total += 1

    def sandwich_add(self):
        '''everytime button is pressed add sandwich'''
        self.sandwich_amount += 4
        self.customer_total += 4


    def cookie_remove(self):
        '''everytime button is pressed remove cookie'''
        if self.cookie_amount >= 1.5:
            self.cookie_amount -= 1.5


    def water_remove(self):
        '''everytime button is pressed remove water'''
        if self.water_amount >= 1:
            self.water_amount -= 1

    def sandwich_remove(self):
        '''everytime button is pressed remove sandwich'''
        if self.sandwich_amount >= 4:
            self.water_amount -= 4


    def shop(self):
        self.menu()
        self.SHOPButton.setHidden(True)
        self.ExitButton.setHidden(False)

    def exit(self):
        '''add up the total cost and label everything''
        self.Add_cookie.setHidden(True)
        self.Add_water.setHidden(True)
        self.Add_sandwich.setHidden(True)
        self.Remove_cookie.setHidden(True)
        self.Remove_water.setHidden(True)
        self.Remove_sandwich.setHidden(True)
        self.menulabel.clear()
        self.ExitButton.setHidden(True)
        self.ReceiptLabel.setText(f"Receipt\nTotal Amount \n cookie =${self.cookie_amount:.2f} \n water = \t ${self.water_amount:.2f} \n sandwich = ${self.sandwich_amount:.2f} \n total = ${self.customer_total:.2f}")

