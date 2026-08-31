"""Basit Hesap Makinesi"""

import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.lbl_number_1 = QtWidgets.QLabel(self)
        self.lbl_number_1.setText("Number 1: ")
        self.lbl_number_1.move(50, 30)

        self.txt_number_1 = QtWidgets.QLineEdit(self)
        self.txt_number_1.move(150, 30)
        self.txt_number_1.resize(200, 32)

        self.lbl_number_2 = QtWidgets.QLabel(self)
        self.lbl_number_2.setText("Number 2: ")
        self.lbl_number_2.move(50, 80)

        self.txt_number_2 = QtWidgets.QLineEdit(self)
        self.txt_number_2.move(150, 80)
        self.txt_number_2.resize(200, 32)

        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("+")
        self.btn_add.move(150, 130)
        self.btn_add.clicked.connect(self.calculate)

        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText("-")
        self.btn_sub.move(150, 170)
        self.btn_sub.clicked.connect(self.calculate)

        self.btn_mult = QtWidgets.QPushButton(self)
        self.btn_mult.setText("*")
        self.btn_mult.move(150, 210)
        self.btn_mult.clicked.connect(self.calculate)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("/")
        self.btn_div.move(150, 250)
        self.btn_div.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(150, 290)

    def calculate(self):
        sender = self.sender()  # Hangi butondan tıklandığı
        operation = sender.text()
        result = 0

        try:
            num1 = float(self.txt_number_1.text())
            num2 = float(self.txt_number_2.text())
            match operation:
                case "+":
                    result = num1 + num2
                case "-":
                    result = num1 - num2
                case "*":
                    result = num1 * num2
                case "/":
                    result = num1 / num2 if num2 != 0 else "DivideZeroError"
                case _:
                    result = "Invalid Operation"
            self.lbl_result.setText(f"Result: {result}")
        except ValueError:
            self.lbl_result.setText("Please enter valid number")


def main():
    app = QApplication(sys.argv)
    win = MainForm()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
