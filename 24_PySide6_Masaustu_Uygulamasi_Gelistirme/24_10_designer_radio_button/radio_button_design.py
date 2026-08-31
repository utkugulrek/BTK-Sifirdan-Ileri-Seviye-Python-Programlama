# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radio_button_design.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(675, 515)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_ulke = QLabel(self.centralwidget)
        self.lbl_ulke.setObjectName(u"lbl_ulke")
        self.lbl_ulke.setGeometry(QRect(100, 340, 181, 101))
        self.lbl_egitim = QLabel(self.centralwidget)
        self.lbl_egitim.setObjectName(u"lbl_egitim")
        self.lbl_egitim.setGeometry(QRect(360, 340, 181, 101))
        self.btn_ulke = QPushButton(self.centralwidget)
        self.btn_ulke.setObjectName(u"btn_ulke")
        self.btn_ulke.setGeometry(QRect(130, 250, 120, 60))
        self.btn_egitim = QPushButton(self.centralwidget)
        self.btn_egitim.setObjectName(u"btn_egitim")
        self.btn_egitim.setGeometry(QRect(400, 250, 120, 60))
        self.group_ulkeler = QGroupBox(self.centralwidget)
        self.group_ulkeler.setObjectName(u"group_ulkeler")
        self.group_ulkeler.setGeometry(QRect(100, 20, 191, 221))
        self.gridLayoutWidget = QWidget(self.group_ulkeler)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 60, 131, 116))
        self.grid_ulkeler = QGridLayout(self.gridLayoutWidget)
        self.grid_ulkeler.setObjectName(u"grid_ulkeler")
        self.grid_ulkeler.setContentsMargins(0, 0, 0, 0)
        self.radio_tr = QRadioButton(self.gridLayoutWidget)
        self.radio_tr.setObjectName(u"radio_tr")

        self.grid_ulkeler.addWidget(self.radio_tr, 0, 0, 1, 1)

        self.radio_deu = QRadioButton(self.gridLayoutWidget)
        self.radio_deu.setObjectName(u"radio_deu")

        self.grid_ulkeler.addWidget(self.radio_deu, 2, 0, 1, 1)

        self.radio_az = QRadioButton(self.gridLayoutWidget)
        self.radio_az.setObjectName(u"radio_az")

        self.grid_ulkeler.addWidget(self.radio_az, 1, 0, 1, 1)

        self.radio_au = QRadioButton(self.gridLayoutWidget)
        self.radio_au.setObjectName(u"radio_au")

        self.grid_ulkeler.addWidget(self.radio_au, 3, 0, 1, 1)

        self.group_egitimler = QGroupBox(self.centralwidget)
        self.group_egitimler.setObjectName(u"group_egitimler")
        self.group_egitimler.setGeometry(QRect(360, 20, 191, 221))
        self.layoutWidget = QWidget(self.group_egitimler)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 60, 106, 116))
        self.grid_egitim = QGridLayout(self.layoutWidget)
        self.grid_egitim.setObjectName(u"grid_egitim")
        self.grid_egitim.setContentsMargins(0, 0, 0, 0)
        self.radio_ilk = QRadioButton(self.layoutWidget)
        self.radio_ilk.setObjectName(u"radio_ilk")

        self.grid_egitim.addWidget(self.radio_ilk, 0, 0, 1, 1)

        self.radio_lise = QRadioButton(self.layoutWidget)
        self.radio_lise.setObjectName(u"radio_lise")

        self.grid_egitim.addWidget(self.radio_lise, 1, 0, 1, 1)

        self.radio_uni = QRadioButton(self.layoutWidget)
        self.radio_uni.setObjectName(u"radio_uni")

        self.grid_egitim.addWidget(self.radio_uni, 2, 0, 1, 1)

        self.radio_yl = QRadioButton(self.layoutWidget)
        self.radio_yl.setObjectName(u"radio_yl")

        self.grid_egitim.addWidget(self.radio_yl, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 675, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_ulke.setText("")
        self.lbl_egitim.setText("")
        self.btn_ulke.setText(QCoreApplication.translate("MainWindow", u"\u00dclke Se\u00e7imi", None))
        self.btn_egitim.setText(QCoreApplication.translate("MainWindow", u"E\u011fitim Se\u00e7imi", None))
        self.group_ulkeler.setTitle(QCoreApplication.translate("MainWindow", u"\u00dclkeler", None))
        self.radio_tr.setText(QCoreApplication.translate("MainWindow", u"T\u00fcrkiye", None))
        self.radio_deu.setText(QCoreApplication.translate("MainWindow", u"Almanya", None))
        self.radio_az.setText(QCoreApplication.translate("MainWindow", u"Azerbaycan", None))
        self.radio_au.setText(QCoreApplication.translate("MainWindow", u"Avusturya", None))
        self.group_egitimler.setTitle(QCoreApplication.translate("MainWindow", u"E\u011fitim D\u00fczeyleri", None))
        self.radio_ilk.setText(QCoreApplication.translate("MainWindow", u"\u0130lkokul", None))
        self.radio_lise.setText(QCoreApplication.translate("MainWindow", u"Lise", None))
        self.radio_uni.setText(QCoreApplication.translate("MainWindow", u"\u00dcniversite", None))
        self.radio_yl.setText(QCoreApplication.translate("MainWindow", u"Y\u00fcksek Lisans", None))
    # retranslateUi

