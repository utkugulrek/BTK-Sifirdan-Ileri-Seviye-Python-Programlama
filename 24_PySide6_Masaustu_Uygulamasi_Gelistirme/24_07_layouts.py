"""Kod üzerinden Yatay, Dikey ve Grid Layout üretimi ve renkler"""

import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))

        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 500)

        h_layout_1 = QtWidgets.QHBoxLayout()  # Yatay
        h_layout_1.addWidget(Color("blue"))
        h_layout_1.addWidget(Color("yellow"))
        h_layout_1.setContentsMargins(50, 0, 0, 0)
        h_layout_1.setSpacing(20)

        h_layout_2 = QtWidgets.QHBoxLayout()  # Yatay
        h_layout_2.addWidget(Color("yellow"))
        h_layout_2.addWidget(Color("blue"))
        h_layout_2.addWidget(Color("yellow"))

        v_layout = QtWidgets.QVBoxLayout()  # Dikey
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        widget = QtWidgets.QWidget()
        widget.setLayout(v_layout)

        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color("blue"), 0, 0)
        # layout.addWidget(Color("yellow"), 1, 0)
        # layout.addWidget(Color("green"), 0, 1)
        # layout.addWidget(Color("blue"), 1, 1)
        # widget = QtWidgets.QWidget()
        # widget.setLayout(layout)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
