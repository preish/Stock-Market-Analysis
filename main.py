import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow #toolkit for GUI
# from PyQt5.QtGui import QIcon

def window():
    # App configurations
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200,300,500,500) # Set starting location for app
    win.setWindowTitle('Stock Market Analysis')
    # win.setWindowIcon(QIcon('image.png')) # Change default window icon

    # Ticker Field
    lbl_ticker = QtWidgets.QLabel(win)
    lbl_ticker.setText('Ticker Symbol: ')
    lbl_ticker.move(50,50)
    txt_ticker = QtWidgets.QLineEdit(win)
    txt_ticker.move(200,50)

    def clicked(self):
        print(f'You entered the ticker symbol {txt_ticker.text().upper()}')

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Search')
    btn_save.clicked.connect(clicked)
    btn_save.move(200,100)

    win.show()
    sys.exit(app.exec_())

window()