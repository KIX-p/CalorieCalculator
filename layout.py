# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 522)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 421, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("gridline-color:{rgb(0, 85, 0)}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.product = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.product.setObjectName("product")
        self.horizontalLayout.addWidget(self.product)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.calories = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.calories.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calories.setInputMethodHints(QtCore.Qt.ImhNone)
        self.calories.setObjectName("calories")
        self.horizontalLayout.addWidget(self.calories)
        self.add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 100, 204, 115))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listofproducts = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listofproducts.setEnabled(False)
        self.listofproducts.setObjectName("listofproducts")
        self.verticalLayout.addWidget(self.listofproducts)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.wynik = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.wynik.setText("")
        self.wynik.setObjectName("wynik")
        self.horizontalLayout_2.addWidget(self.wynik)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.img = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img.setText("")
        self.img.setObjectName("img")
        self.verticalLayout.addWidget(self.img)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 220, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 230, 172, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.femaleradio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.femaleradio.setEnabled(True)
        self.femaleradio.setChecked(True)
        self.femaleradio.setObjectName("femaleradio")
        self.horizontalLayout_3.addWidget(self.femaleradio)
        self.maleradio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.maleradio.setObjectName("maleradio")
        self.horizontalLayout_3.addWidget(self.maleradio)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 310, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bigactivityradio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.bigactivityradio.setChecked(True)
        self.bigactivityradio.setObjectName("bigactivityradio")
        self.verticalLayout_2.addWidget(self.bigactivityradio)
        self.mediumactivityradio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.mediumactivityradio.setObjectName("mediumactivityradio")
        self.verticalLayout_2.addWidget(self.mediumactivityradio)
        self.smallactivityradio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.smallactivityradio.setObjectName("smallactivityradio")
        self.verticalLayout_2.addWidget(self.smallactivityradio)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nazwa posiłku"))
        self.label_2.setText(_translate("Dialog", "Liczba kalorii"))
        self.add.setText(_translate("Dialog", "Dodaj"))
        self.label_3.setText(_translate("Dialog", "Suma spozytych kalorii: "))
        self.femaleradio.setText(_translate("Dialog", "Kobieta"))
        self.maleradio.setText(_translate("Dialog", "Mężczyzna"))
        self.bigactivityradio.setText(_translate("Dialog", "Duza aktywnosc"))
        self.mediumactivityradio.setText(_translate("Dialog", "Srednia aktywnosc"))
        self.smallactivityradio.setText(_translate("Dialog", "mala aktywnosc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())