import sys
from PyQt5.QtWidgets import QApplication, QMainWindow #toolkit for GUI
# from PyQt5.QtGui import QIcon

# Configure app
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200,300,500,500) # Set starting location for app
    win.setWindowTitle('Stock Market Analysis')
    # win.setWindowIcon(QIcon('image.png')) # Change default window icon
    win.show()
    sys.exit(app.exec_())

window()