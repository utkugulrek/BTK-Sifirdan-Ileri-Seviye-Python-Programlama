"""Combo Box Kullanımı"""

import sys

from PySide6 import QtWidgets

from combo_box_design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.combo_sehirler
        combo.addItem("İstanbul")
        combo.addItem("Sinop")
        # combo.addItems(["Kocaeli", "İzmir", "Ankara"])

        self.ui.btn_load_items.clicked.connect(self.load_items)
        self.ui.btn_get_item.clicked.connect(self.get_item)
        self.ui.btn_clear_items.clicked.connect(self.clear_items)

        combo.currentIndexChanged.connect(self.selected_changed_index)  # O an tıklananın index'i
        # combo.currentIndexChanged[str].connect(self.selected_changed_text)  # Eskidi
        combo.currentTextChanged.connect(self.selected_changed_text)  # O an tıklananın text'i

    def load_items(self):
        sehirler = ["Kocaeli", "İzmir", "Ankara"]
        self.ui.combo_sehirler.addItems(sehirler)

    def get_item(self):
        print(self.ui.combo_sehirler.currentText())
        print(self.ui.combo_sehirler.currentIndex())  # Index

        count = self.ui.combo_sehirler.count()
        print(f"Tüm Şehirler: {count}".center(20, "-"))  # Eleman sayısı
        for index in range(count):
            print(self.ui.combo_sehirler.itemText(index))

    def selected_changed_index(self, index):  # O an seçilenin indeks bilgisi
        print(index)

    def selected_changed_text(self, text):  # O an seçilenin text  bilgisi
        print(text)

    def clear_items(self):
        self.ui.combo_sehirler.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
