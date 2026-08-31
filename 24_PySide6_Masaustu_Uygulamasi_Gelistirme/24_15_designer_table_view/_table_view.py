"""Table View Kullanımı"""

import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem

from table_view_design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_products()
        self.ui.btn_save.clicked.connect(self.save_product)

        self.ui.table_products.doubleClicked.connect(self.double_click)

    def load_products(self):

        products = [
            {"name": "iPhone 5S", "price": "5000"},
            {"name": "iPhone 11", "price": "8000"},
            {"name": "iPhone 13", "price": "12000"},
            {"name": "iPhone 15", "price": "17000"},
        ]

        self.ui.table_products.setRowCount(len(products))  # Database için dinamik oluşturulur
        self.ui.table_products.setColumnCount(2)
        self.ui.table_products.setHorizontalHeaderLabels(("Name", "Price"))  # Kolon adlandırma
        self.ui.table_products.setColumnWidth(0, 100)  # Kolon Genişliği
        self.ui.table_products.setColumnWidth(1, 50)

        for row_index, product in enumerate(products):
            self.ui.table_products.setItem(row_index, 0, QTableWidgetItem(product["name"]))
            self.ui.table_products.setItem(row_index, 1, QTableWidgetItem(product["price"]))

        # self.ui.table_products.setItem(0, 0, QTableWidgetItem("iPhone 5S"))
        # self.ui.table_products.setItem(0, 1, QTableWidgetItem("2000"))

        # self.ui.table_products.setItem(1, 0, QTableWidgetItem("iPhone 11"))
        # self.ui.table_products.setItem(1, 1, QTableWidgetItem("7000"))

        # self.ui.table_products.setItem(2, 0, QTableWidgetItem("iPhone 13"))
        # self.ui.table_products.setItem(2, 1, QTableWidgetItem("10000"))

    def save_product(self):
        name = self.ui.txt_name.text()
        price = self.ui.txt_price.text()

        if name.strip() and price.strip():
            row_count = self.ui.table_products.rowCount()
            self.ui.table_products.insertRow(row_count)
            self.ui.table_products.setItem(row_count, 0, QTableWidgetItem(name))
            self.ui.table_products.setItem(row_count, 1, QTableWidgetItem(price))

            self.ui.txt_name.clear()  # Text'i temizler
            self.ui.txt_price.clear()

    def double_click(self):
        for item in self.ui.table_products.selectedItems():
            print(item.row(), item.column(), item.text())


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
