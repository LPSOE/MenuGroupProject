from PyQt5.QtWidgets import *
from controller import *

'Feedback'
'ToDo Add Edit to Quantity'


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
