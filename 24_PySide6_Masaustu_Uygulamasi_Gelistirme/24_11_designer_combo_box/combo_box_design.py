# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'combo_box_design.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(618, 279)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.combo_sehirler = QComboBox(self.centralwidget)
        self.combo_sehirler.setObjectName(u"combo_sehirler")
        self.combo_sehirler.setGeometry(QRect(130, 60, 171, 41))
        self.btn_clear_items = QPushButton(self.centralwidget)
        self.btn_clear_items.setObjectName(u"btn_clear_items")
        self.btn_clear_items.setGeometry(QRect(320, 80, 131, 41))
        self.btn_load_items = QPushButton(self.centralwidget)
        self.btn_load_items.setObjectName(u"btn_load_items")
        self.btn_load_items.setGeometry(QRect(320, 30, 131, 41))
        self.btn_get_item = QPushButton(self.centralwidget)
        self.btn_get_item.setObjectName(u"btn_get_item")
        self.btn_get_item.setGeometry(QRect(200, 140, 171, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 618, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_clear_items.setText(QCoreApplication.translate("MainWindow", u"Clear Items", None))
        self.btn_load_items.setText(QCoreApplication.translate("MainWindow", u"Load Items", None))
        self.btn_get_item.setText(QCoreApplication.translate("MainWindow", u"Get Item", None))
    # retranslateUi

