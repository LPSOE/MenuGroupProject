from Menu import *
from PyQt5.QtWidgets import *


class Controller(QMainWindow, Ui_LabMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.SHOPButton.clicked.connect(lambda: self.shop())
        self.ExitButton.clicked.connect(lambda: self.exit())

        self.menulabel.setText(f"               Welcome \n\n\n              Customers!")

        self.SHOPButton.setHidden(False)
        self.ExitButton.setHidden(True)
        self.lineEditCookie.setHidden(True)
        self.lineEditSandwich.setHidden(True)
        self.lineEditWater.setHidden(True)
        self.ReceiptLabel.setHidden(True)

        self.cookie_label.setHidden(True)
        self.sandwich_label.setHidden(True)
        self.water_label.setHidden(True)

        self.cookieError_label.setHidden(True)
        self.sandwichError_label.setHidden(True)
        self.waterError_label.setHidden(True)

        self.cookie = float(1.50)
        self.sandwich = float(4.00)
        self.water = float(1.00)
        # self.customer_total = float(0.00)
        # self.customer_totalCookie = 0

        self.tax = float(0.10)
        self.total_tax = float(0)
    def menu(self):
        self.menulabel.setText(f"\n\n--Lah's Bakery Menu--\n\n     Cookie - $1.50\n\n     Sandwich - $4.00\n\n     Water - $1.00")

    #Show Line Edit
        self.lineEditCookie.setHidden(False)
        self.lineEditSandwich.setHidden(False)
        self.lineEditWater.setHidden(False)

    #Show Quantity Label
        self.cookie_label.setHidden(False)
        self.sandwich_label.setHidden(False)
        self.water_label.setHidden(False)

    def shop(self):
        self.menu()
        self.SHOPButton.setHidden(True)
        self.ExitButton.setHidden(False)

    def exit(self):
    #add up the total cost and label everything
        self.menulabel.clear()
        self.ExitButton.setHidden(True)

        self.cookieError_label.setHidden(False)
        self.sandwichError_label.setHidden(False)
        self.waterError_label.setHidden(False)

        self.cookie_label.setHidden(True)
        self.sandwich_label.setHidden(True)
        self.water_label.setHidden(True)


        self.receipt()



    def receipt(self):
        self.ReceiptLabel.setHidden(False)
        self.cookie_label.setHidden(True)
        self.sandwich_label.setHidden(True)
        self.water_label.setHidden(True)

        self.lineEditCookie.setHidden(True)
        self.lineEditSandwich.setHidden(True)
        self.lineEditWater.setHidden(True)

        self.cookieError_label.setHidden(False)
        self.sandwichError_label.setHidden(False)
        self.waterError_label.setHidden(False)

        try:
            cookie_amount = int(self.lineEditCookie.text())
            sandwich_amount = int(self.lineEditSandwich.text())
            water_amount = int(self.lineEditWater.text())
            customer_total = cookie_amount + sandwich_amount + water_amount
            self.ReceiptLabel.setText(f"{customer_total}")
        except ValueError:
            self.cookieError_label.setText("Invalid Input")

    def error_handling(self):
        pass




