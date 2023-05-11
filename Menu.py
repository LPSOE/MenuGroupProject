# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LabMenu(object):
    def setupUi(self, LabMenu):
        LabMenu.setObjectName("LabMenu")
        LabMenu.setEnabled(True)
        LabMenu.resize(600, 600)
        LabMenu.setMinimumSize(QtCore.QSize(600, 600))
        LabMenu.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setPointSize(30)
        LabMenu.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LabMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.menulabel = QtWidgets.QLabel(self.centralwidget)
        self.menulabel.setGeometry(QtCore.QRect(120, 30, 381, 331))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.menulabel.setFont(font)
        self.menulabel.setObjectName("menulabel")
        self.SHOPButton = QtWidgets.QPushButton(self.centralwidget)
        self.SHOPButton.setGeometry(QtCore.QRect(210, 400, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SHOPButton.setFont(font)
        self.SHOPButton.setObjectName("SHOPButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(240, 420, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        self.ReceiptLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReceiptLabel.setGeometry(QtCore.QRect(120, 90, 411, 311))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ReceiptLabel.setFont(font)
        self.ReceiptLabel.setText("")
        self.ReceiptLabel.setObjectName("ReceiptLabel")
        self.lineEditCookie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCookie.setGeometry(QtCore.QRect(280, 210, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEditCookie.setFont(font)
        self.lineEditCookie.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditCookie.setText("")
        self.lineEditCookie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditCookie.setObjectName("lineEditCookie")
        self.lineEditSandwich = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSandwich.setGeometry(QtCore.QRect(280, 290, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEditSandwich.setFont(font)
        self.lineEditSandwich.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditSandwich.setObjectName("lineEditSandwich")
        self.lineEditWater = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWater.setGeometry(QtCore.QRect(280, 360, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEditWater.setFont(font)
        self.lineEditWater.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditWater.setObjectName("lineEditWater")
        self.cookie_label = QtWidgets.QLabel(self.centralwidget)
        self.cookie_label.setGeometry(QtCore.QRect(200, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cookie_label.setFont(font)
        self.cookie_label.setObjectName("cookie_label")
        self.sandwich_label = QtWidgets.QLabel(self.centralwidget)
        self.sandwich_label.setGeometry(QtCore.QRect(200, 290, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sandwich_label.setFont(font)
        self.sandwich_label.setObjectName("sandwich_label")
        self.water_label = QtWidgets.QLabel(self.centralwidget)
        self.water_label.setGeometry(QtCore.QRect(200, 370, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.water_label.setFont(font)
        self.water_label.setObjectName("water_label")
        self.Error_label = QtWidgets.QLabel(self.centralwidget)
        self.Error_label.setGeometry(QtCore.QRect(420, 230, 161, 131))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Error_label.setFont(font)
        self.Error_label.setObjectName("Error_label")
        self.sandwichpix = QtWidgets.QLabel(self.centralwidget)
        self.sandwichpix.setGeometry(QtCore.QRect(20, 380, 151, 171))
        self.sandwichpix.setText("")
        self.sandwichpix.setPixmap(QtGui.QPixmap("Screenshot 2023-05-11 at 5.15.05 PM.png"))
        self.sandwichpix.setScaledContents(True)
        self.sandwichpix.setObjectName("sandwichpix")
        self.cookiepix = QtWidgets.QLabel(self.centralwidget)
        self.cookiepix.setGeometry(QtCore.QRect(410, 380, 161, 151))
        self.cookiepix.setText("")
        self.cookiepix.setPixmap(QtGui.QPixmap("Screenshot 2023-05-11 at 5.14.46 PM.png"))
        self.cookiepix.setScaledContents(True)
        self.cookiepix.setObjectName("cookiepix")
        self.waterpix = QtWidgets.QLabel(self.centralwidget)
        self.waterpix.setGeometry(QtCore.QRect(480, 30, 111, 201))
        self.waterpix.setText("")
        self.waterpix.setPixmap(QtGui.QPixmap("Screenshot 2023-05-11 at 5.14.24 PM.png"))
        self.waterpix.setScaledContents(True)
        self.waterpix.setObjectName("waterpix")
        LabMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LabMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 24))
        self.menubar.setObjectName("menubar")
        self.menucolors = QtWidgets.QMenu(self.menubar)
        self.menucolors.setObjectName("menucolors")
        LabMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LabMenu)
        self.statusbar.setObjectName("statusbar")
        LabMenu.setStatusBar(self.statusbar)
        self.actioncolors = QtWidgets.QAction(LabMenu)
        self.actioncolors.setObjectName("actioncolors")
        self.menucolors.addAction(self.actioncolors)
        self.menubar.addAction(self.menucolors.menuAction())

        self.retranslateUi(LabMenu)
        QtCore.QMetaObject.connectSlotsByName(LabMenu)

    def retranslateUi(self, LabMenu):
        _translate = QtCore.QCoreApplication.translate
        LabMenu.setWindowTitle(_translate("LabMenu", "MainWindow"))
        self.menulabel.setText(_translate("LabMenu", "Welcome"))
        self.SHOPButton.setText(_translate("LabMenu", "SHOP"))
        self.ExitButton.setText(_translate("LabMenu", "EXIT"))
        self.cookie_label.setText(_translate("LabMenu", "Quantity:"))
        self.sandwich_label.setText(_translate("LabMenu", "Quantity:"))
        self.water_label.setText(_translate("LabMenu", "Quantity:"))
        self.Error_label.setText(_translate("LabMenu", "TextLabel"))
        self.menucolors.setTitle(_translate("LabMenu", "colors"))
        self.actioncolors.setText(_translate("LabMenu", "colors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabMenu = QtWidgets.QMainWindow()
    ui = Ui_LabMenu()
    ui.setupUi(LabMenu)
    LabMenu.show()
    sys.exit(app.exec_())
