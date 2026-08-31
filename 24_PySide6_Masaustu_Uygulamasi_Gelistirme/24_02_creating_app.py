"""
PyQt5, Python3.14+ ile optimum çalışmadığı için
PySide6 ile devam edildi.
İlk masaüstü uygulamasını oluşturma
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon


def create_window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Application")  # Pencere başlığı
    win.setGeometry(200, 200, 500, 500)  # İlk ikisi konum, son ikisi boyut
    win.setWindowIcon(QIcon("utk_logo.png"))
    win.setToolTip("My ToolTip")  # Uygulamanın üzerinde mouse bıraktığımızda yazan

    win.show()
    sys.exit(app.exec())  # Kapat butonu için


create_window()
