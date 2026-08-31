"""Radio Button Kullanımı"""

import sys

from PySide6 import QtWidgets

from radio_button_design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radio_tr.setChecked(True)  # Default seçili
        self.ui.radio_lise.setChecked(True)
        # Butonları döngü ile kontrol
        groups = [self.ui.group_ulkeler, self.ui.group_egitimler]
        for group in groups:
            for rb in group.findChildren(QtWidgets.QRadioButton):
                rb.toggled.connect(self.on_clicked)

        self.ui.btn_ulke.clicked.connect(self.get_selected_ulke)
        self.ui.btn_egitim.clicked.connect(self.get_selected_egitim)

    def on_clicked(self):
        rb = self.sender()
        if rb.isChecked():
            print(f"Seçiminiz: {rb.text()}")

    def get_selected_ulke(self):
        rbs = self.ui.group_ulkeler.findChildren(QtWidgets.QRadioButton)
        for rb in rbs:
            if rb.isChecked():
                self.ui.lbl_ulke.setText(f"Seçiminiz: {rb.text()}")

    def get_selected_egitim(self):
        rbs = self.ui.group_egitimler.findChildren(QtWidgets.QRadioButton)
        for rb in rbs:
            if rb.isChecked():
                self.ui.lbl_egitim.setText(f"Seçiminiz: {rb.text()}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
