"""PySide6 ile pencere elemanları"""

import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon


def create_window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    # Pencere Ayarları
    win.setWindowTitle("First Application")
    win.setGeometry(200, 200, 500, 500)
    win.setWindowIcon(QIcon("utk_logo.png"))
    win.setToolTip("My ToolTip")

    # Text Ekleme
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Name: ")
    lbl_name.move(50, 30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Surame: ")
    lbl_surname.move(50, 70)

    # Input Text Kutusu
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(95, 30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(95, 70)

    # Butona Tıklandığında
    def clicked(self):
        print(f"Clicked by N: {txt_name.text()} S: {txt_surname.text()}")

    # Buton
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.move(95, 110)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())


create_window()
