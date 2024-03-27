from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1479, 881)
        Form.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.baslat = QtWidgets.QPushButton(Form)
        self.baslat.setGeometry(QtCore.QRect(1120, 40, 341, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.baslat.setFont(font)
        self.baslat.setStyleSheet("background-color: rgb(159, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.baslat.setObjectName("baslat")
        self.veriaktar = QtWidgets.QTableWidget(Form)
        self.veriaktar.setGeometry(QtCore.QRect(25, 121, 1431, 741))
        self.veriaktar.setObjectName("veriaktar")
        self.veriaktar.setColumnCount(0)
        self.veriaktar.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IoT Windows 10 Attack Detection"))
        self.baslat.setText(_translate("Form", "ANALİZE BAŞLA"))
