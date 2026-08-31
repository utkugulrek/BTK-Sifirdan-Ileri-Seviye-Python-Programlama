"""PySide6 ile Pencere Sınıfının Genişletilmesi (OOP Mimarisi)"""

import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon


# Miras inheritance alıyor QMainWindow'dan
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Pencere Ayarları
        self.setWindowTitle("First Application")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowIcon(QIcon("utk_logo.png"))
        self.setToolTip("My ToolTip")
        self.initUI()

    # Pencere Elemanlarının Ayarlandığı
    def initUI(self):
        # Text Ekleme
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Name: ")
        self.lbl_name.move(50, 30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surame: ")
        self.lbl_surname.move(50, 70)

        # Input Text Kutusu
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(95, 30)
        self.txt_name.resize(200, 32)  # Box Boyutu

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(95, 70)
        self.txt_surname.resize(200, 32)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(95, 150)
        self.lbl_result.resize(300, 50)

        # Buton
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(95, 110)
        self.btn_save.clicked.connect(self.clicked)

    # Butona Tıklandığında
    def clicked(self):
        self.lbl_result.setText(
            f"Name: {self.txt_name.text()} Surname: {self.txt_surname.text()}"
        )


def create_window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())


create_window()
