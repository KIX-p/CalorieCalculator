import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog



class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setStyleSheet("color: rgb(0, 85, 0)")
        self.ui.label_2.setStyleSheet("color: rgb(0, 85, 0)")
        self.ui.add.setStyleSheet("background-color: rgb(0, 255, 127); font-weight: bold")
        self.ui.label_3.setStyleSheet("color: white; background-color: green;")
        self.ui.add.clicked.connect(self.add)
        self.sum = 0

    def add(self):
        meal = self.ui.product.text()
        kcal = self.ui.calories.text()
        self.sum += float(kcal)
        self.ui.listofproducts.addItem(f'{meal} - {kcal}')
        self.ui.wynik.setText(f'{self.sum}')

        if self.sum < 1700 and self.ui.smallactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: green")
            self.ui.img.setPixmap(QPixmap("1.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum == 1700 and self.ui.smallactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: black")
            self.ui.img.setPixmap(QPixmap("2.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum >= 1700 and self.ui.smallactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: red")
            self.ui.img.setPixmap(QPixmap("3.jpg"))
            self.ui.img.setScaledContents(True)

        if self.sum < 1900 and self.ui.mediumactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: green")
            self.ui.img.setPixmap(QPixmap("1.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum == 1900 and self.ui.mediumactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: black")
            self.ui.img.setPixmap(QPixmap("2.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum >= 1900 and self.ui.mediumactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: red")
            self.ui.img.setPixmap(QPixmap("3.jpg"))
            self.ui.img.setScaledContents(True)

        if self.sum < 2100 and self.ui.bigactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: green")
            self.ui.img.setPixmap(QPixmap("1.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum == 2100 and self.ui.bigactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: black")
            self.ui.img.setPixmap(QPixmap("2.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum >= 2100 and self.ui.bigactivityradio.isChecked() and self.ui.femaleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: red")
            self.ui.img.setPixmap(QPixmap("3.jpg"))
            self.ui.img.setScaledContents(True)

        if self.sum < 1900 and self.ui.smallactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: green")
            self.ui.img.setPixmap(QPixmap("1.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum == 1900 and self.ui.smallactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: black")
            self.ui.img.setPixmap(QPixmap("2.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum >= 1900 and self.ui.smallactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: red")
            self.ui.img.setPixmap(QPixmap("3.jpg"))
            self.ui.img.setScaledContents(True)

        if self.sum < 2200 and self.ui.mediumactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: green")
            self.ui.img.setPixmap(QPixmap("1.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum == 2200 and self.ui.mediumactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: black")
            self.ui.img.setPixmap(QPixmap("2.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum >= 2200 and self.ui.mediumactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: red")
            self.ui.img.setPixmap(QPixmap("3.jpg"))
            self.ui.img.setScaledContents(True)

        if self.sum < 2500 and self.ui.bigactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: green")
            self.ui.img.setPixmap(QPixmap("1.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum == 2500 and self.ui.bigactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: black")
            self.ui.img.setPixmap(QPixmap("2.jpg"))
            self.ui.img.setScaledContents(True)
        elif self.sum >= 2500 and self.ui.bigactivityradio.isChecked() and self.ui.maleradio.isChecked():
            self.ui.wynik.setStyleSheet("color: red")
            self.ui.img.setPixmap(QPixmap("3.jpg"))
            self.ui.img.setScaledContents(True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    w.setWindowTitle("kalkulator kalorii")
    sys.exit(app.exec_())
