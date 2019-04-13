from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtCore, QtWidgets, QtGui
import sys


from testgui import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setImage)



    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)

    if __name__ == "__main__":
	    import sys
	    app = QtWidgets.QApplication(sys.argv)
	    MainWindow = QtWidgets.QMainWindow()
	    ui = Ui_MainWindow()
	    ui.setupUi(MainWindow)
	    MainWindow.show()
	    sys.exit(app.exec_())