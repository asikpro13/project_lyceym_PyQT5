# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from DataBase.workFromDB import DB


class addProductWindow(QtWidgets.QDialog):
    def __init__(self, root):
        self.root = root
        self.root.setEnabled(False)
        self.db = self.root.db
        super(addProductWindow, self).__init__()

        self.pushButton = QtWidgets.QPushButton(self)

        self.setupUi()

    def setupUi(self):
        self.resize(380, 499)
        self.pushButton.setGeometry(QtCore.QRect(130, 450, 93, 28))
        self.pushButton.clicked.connect(self.createProduct)
        self.warning = QtWidgets.QLabel(self)
        self.warning.setText('Ошибка')
        self.warning.hide()
        self.warning.move(self.width() // 2 - self.warning.width() // 2, 5)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 280, 55, 16))
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(150, 280, 141, 22))
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 320, 140, 22))
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(70, 320, 50, 20))
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(70, 360, 55, 16))
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(70, 400, 80, 16))
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(80, 0, 241, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 150, 150))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border-style: solid;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 75%;\n"
                                        "border-color: red;}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(200, 200, 200);}")
        self.pushButton_2.clicked.connect(self.addPhoto)
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(150, 400, 141, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000000)
        self.spinBox_2 = QtWidgets.QSpinBox(self)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 360, 141, 22))
        self.spinBox_2.setMaximum(1000000000)
        self.label_6 = QtWidgets.QLabel(self)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addPhoto(self):
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть изображение товара', filter='Файлы изображений (*.png *.jpg *.bmp)')
        self.label_6.move(20, 70)
        self.pixmap = QtGui.QPixmap(self.fname)
        self.pixmap = self.pixmap.scaled(QtCore.QSize(150, 200))
        self.label_6.resize(150, 200)
        self.label_6.setPixmap(self.pixmap)

    def createProduct(self):
        try:
            self.db.addProduct(self.fname, self.lineEdit.text(), self.lineEdit_2.text(), self.spinBox_2.text(), self.spinBox.text())
            self.close()
        except FileNotFoundError:
            self.warning.show()
        except AttributeError:
            self.warning.show()

    def closeEvent(self, Event):  # Макрос от pyqt срабатывающий при закрытии окна
        self.root.setEnabled(True)  # Говорим окну продолжить работу
        self.root.updateTable()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Добавление продукта"))
        self.pushButton.setText(_translate("Form", "Создать"))
        self.label.setText(_translate("Form", "Бренд"))
        self.label_2.setText(_translate("Form", "Модель"))
        self.label_3.setText(_translate("Form", "Цена"))
        self.label_4.setText(_translate("Form", "Количество"))
        self.label_5.setText(_translate("Form", "Создание товара"))
        self.pushButton_2.setText(_translate("Form", "добавить фото"))
