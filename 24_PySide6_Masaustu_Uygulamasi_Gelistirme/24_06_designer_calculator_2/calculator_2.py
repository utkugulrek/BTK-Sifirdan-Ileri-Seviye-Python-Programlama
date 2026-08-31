"""Designer'dan gelmiş UI ile tekrar hesap makinesi oluşturma"""

import sys

from PySide6 import QtWidgets

from first_design import Ui_MainWindow


class App(QtWidgets.QMainWindow):  # TASARIM kısmı
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Butonları döngüyle tıklatma
        buttons = [self.ui.btn_add, self.ui.btn_sub, self.ui.btn_mult, self.ui.btn_div]
        for btn in buttons:
            btn.clicked.connect(self.calculate)

    def calculate(self):
        sender = self.sender()  # Hangi butondan tıklandığı
        operation = sender.text()
        result = 0

        try:
            num1 = float(self.ui.txt_number_1.text())
            num2 = float(self.ui.txt_number_2.text())
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
            self.ui.lbl_result.setText(f"= {result}")
        except ValueError:
            self.ui.lbl_result.setText("Please enter valid number")


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
