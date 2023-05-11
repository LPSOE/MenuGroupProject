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

        self.Error_label.setHidden(True)


        self.cookie = float(1.50)
        self.sandwich = float(4.00)
        self.water = float(1.00)
        self.customer_total = float(0.00)
        self.cookie_amount = 0
        self.sandwich_amount = 0
        self.water_amount = 0

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

        self.Error_label.setHidden(False)

        self.waterpix.setHidden(True)
        self.sandwichpix.setHidden(True)
        self.cookiepix.setHidden(True)

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

        self.Error_label.setHidden(True)

        try:
            self.cookie_amount = int(self.lineEditCookie.text())
            self.sandwich_amount = int(self.lineEditSandwich.text())
            self.water_amount = int(self.lineEditWater.text())
            self.formula()
        except ValueError:
            self.error_handling()
            self.Error_label.setText("Error Message: \nCookie, Sandwich,\n and Water\nNeed to be numeric\nEnter: 0 for Item\n Not Wanted")

    def formula(self):
    #Tally up all the customer order and taxes
        self.customer_total = (self.cookie_amount * self.cookie) + (self.sandwich_amount * self.sandwich) + (self.water_amount * self.water)
        self.total_tax = self.tax * self.customer_total
        self.ReceiptLabel.setText(f"\t\tReceipt\n\n"
                                  f"({self.cookie_amount})Cookie(s)______________________${self.cookie_amount * self.cookie:.2f}\n"
                                  f"({self.sandwich_amount})Sandwich(s)____________________${self.sandwich_amount * self.sandwich:.2f}\n"
                                  f"({self.water_amount})Water(s)_______________________${self.water_amount * self.water:.2f}\n"
                                  f"\n\n\n\n\n"
                                  f"Tax_____________________________{self.tax:.2f}%\n"
                                  f"Total Amount______________________${self.customer_total + self.total_tax:.2f}")

    def error_handling(self):
    #if String and Float entered error_handling will be initiated
        self.menu()
        self.ExitButton.setHidden(False)
        self.cookie_label.setHidden(False)
        self.sandwich_label.setHidden(False)
        self.water_label.setHidden(False)

        self.lineEditCookie.setHidden(False)
        self.lineEditSandwich.setHidden(False)
        self.lineEditWater.setHidden(False)

        self.Error_label.setHidden(False)




