# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_design.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(679, 188)
        self.actionsa_Turk_war_m = QAction(MainWindow)
        self.actionsa_Turk_war_m.setObjectName(u"actionsa_Turk_war_m")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_number_1 = QLabel(self.centralwidget)
        self.lbl_number_1.setObjectName(u"lbl_number_1")
        self.lbl_number_1.setGeometry(QRect(30, 30, 81, 21))
        self.lbl_number_2 = QLabel(self.centralwidget)
        self.lbl_number_2.setObjectName(u"lbl_number_2")
        self.lbl_number_2.setGeometry(QRect(30, 80, 81, 21))
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(250, 55, 41, 31))
        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        self.btn_sub.setGeometry(QRect(300, 55, 41, 31))
        self.btn_mult = QPushButton(self.centralwidget)
        self.btn_mult.setObjectName(u"btn_mult")
        self.btn_mult.setGeometry(QRect(350, 55, 41, 31))
        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setGeometry(QRect(400, 55, 41, 31))
        self.lbl_result = QLabel(self.centralwidget)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setGeometry(QRect(450, 55, 201, 31))
        self.txt_number_1 = QLineEdit(self.centralwidget)
        self.txt_number_1.setObjectName(u"txt_number_1")
        self.txt_number_1.setGeometry(QRect(100, 30, 113, 26))
        self.txt_number_2 = QLineEdit(self.centralwidget)
        self.txt_number_2.setObjectName(u"txt_number_2")
        self.txt_number_2.setGeometry(QRect(100, 80, 113, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 679, 33))
        self.menuUTK = QMenu(self.menubar)
        self.menuUTK.setObjectName(u"menuUTK")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuUTK.menuAction())
        self.menuUTK.addAction(self.actionsa_Turk_war_m)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsa_Turk_war_m.setText(QCoreApplication.translate("MainWindow", u"sa Turk war m\u0131", None))
        self.lbl_number_1.setText(QCoreApplication.translate("MainWindow", u"Number 1", None))
        self.lbl_number_2.setText(QCoreApplication.translate("MainWindow", u"Number 2", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.lbl_result.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.txt_number_1.setText("")
        self.txt_number_2.setText("")
        self.menuUTK.setTitle(QCoreApplication.translate("MainWindow", u"UTK", None))
    # retranslateUi

