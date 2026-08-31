"""CheckBox Kullanımı"""

import sys

from PySide6 import QtWidgets

from checkbox_design import Ui_MainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_movies.stateChanged.connect(self.show_state)
        self.ui.cb_reading.stateChanged.connect(self.show_state)
        self.ui.cb_sports.stateChanged.connect(self.show_state)

        self.ui.btn_get_hobbies.clicked.connect(self.get_all_hobbies)
        self.ui.btn_get_lectures.clicked.connect(self.get_all_lectures)


    def get_all_hobbies(self):
        result = ""
        checkboxes = self.ui.group_hobbies.findChildren(QtWidgets.QCheckBox)
        for cb in checkboxes:
            if cb.isChecked():
                result += cb.text() + "\n"
        self.ui.lbl_result_hobbies.setText(result)

    def show_state(self, value):
        cb = self.sender()
        # print(value)  # Seçili ise konsola 2 yazar, çekince 0
        # print(cb.isChecked())  # True, False
        # print(cb.text())

    def get_all_lectures(self):
        result = ""
        checkboxes = self.ui.group_lectures.findChildren(QtWidgets.QCheckBox)
        for cb in checkboxes:
            if cb.isChecked():
                result += cb.text() + "\n"
        self.ui.lbl_result_lectures.setText(result)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
