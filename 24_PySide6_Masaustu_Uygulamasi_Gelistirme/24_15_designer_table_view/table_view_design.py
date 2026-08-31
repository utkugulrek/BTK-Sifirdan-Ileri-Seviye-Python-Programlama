# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_view_design.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 329)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table_products = QTableWidget(self.centralwidget)
        self.table_products.setObjectName(u"table_products")
        self.table_products.setGeometry(QRect(40, 60, 251, 181))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(320, 100, 160, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_name_2 = QLabel(self.formLayoutWidget)
        self.lbl_name_2.setObjectName(u"lbl_name_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_name_2)

        self.lbl_name = QLabel(self.formLayoutWidget)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_name)

        self.txt_name = QLineEdit(self.formLayoutWidget)
        self.txt_name.setObjectName(u"txt_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_name)

        self.txt_price = QLineEdit(self.formLayoutWidget)
        self.txt_price.setObjectName(u"txt_price")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_price)

        self.btn_save = QPushButton(self.formLayoutWidget)
        self.btn_save.setObjectName(u"btn_save")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btn_save)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 562, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_name_2.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

