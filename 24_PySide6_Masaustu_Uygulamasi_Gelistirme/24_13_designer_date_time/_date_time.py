"""Date & Time Kullanımı"""

import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QDate

from date_time_design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_calculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.date_starting.date()
        end = self.ui.date_ending.date()
        print(start, end)

        print(f"Days in month: {start.daysInMonth()}")  # Aydaki gün sayısı
        print(f"Days in year: {start.daysInYear()}")  # Yıldaki gün sayısı

        print(f"Days between dates {start.daysTo(end)}")  # 1'den 2'ye gün sayısı

        now = QDate.currentDate()  # Bugün
        print(f"Total days from now {start.daysTo(now)}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
