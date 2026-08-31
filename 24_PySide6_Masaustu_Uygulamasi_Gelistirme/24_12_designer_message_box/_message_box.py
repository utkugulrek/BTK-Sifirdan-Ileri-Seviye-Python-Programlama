"""Message Box Kullanımı"""

import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from message_box_design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.show_dialog)

    def show_dialog(self):
        # Kısa Yol
        result = QMessageBox.question(
            self,
            "Close Application",  # Başlık
            "Are you sure?",  # Mesaj
            QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,  # Seçenekler
            QMessageBox.Cancel,  # Default Seçim
        )
        if result == QMessageBox.Ok:
            print("Quiting...")
            QtWidgets.QApplication.quit()

    ####################################################################################################
    # Uzun yol

    # msg = QMessageBox()

    # msg.setWindowTitle("Close Application")
    # msg.setText("Are you sure?")
    # msg.setIcon(QMessageBox.Question)  # Soru icon'u
    # msg.setIcon(QMessageBox.Warning)  # Ünlem, dikkat icon'u
    # # Butonlar
    # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)

    # msg.setDefaultButton(QMessageBox.Cancel)  # Mavi yanarak gelir

    # msg.setDetailedText("details...")
    # msg.buttonClicked.connect(self.popup_button)

    # x = msg.exec()  # Seçim
    # print(x)

    def popup_button(self, i):
        print(i.text())
        i_text = i.text()

        if i_text == "OK":
            print("OKAYY")
            # QtWidgets.qApp.quit()  # Eski
            QtWidgets.QApplication.quit()
        elif i_text == "Cancel":
            print("Canceling")
        else:
            print("Ignoring")


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
