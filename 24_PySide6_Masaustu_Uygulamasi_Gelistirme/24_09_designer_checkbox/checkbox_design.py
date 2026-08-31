# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkbox_design.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_result_hobbies = QLabel(self.centralwidget)
        self.lbl_result_hobbies.setObjectName(u"lbl_result_hobbies")
        self.lbl_result_hobbies.setGeometry(QRect(60, 270, 161, 121))
        self.btn_get_hobbies = QPushButton(self.centralwidget)
        self.btn_get_hobbies.setObjectName(u"btn_get_hobbies")
        self.btn_get_hobbies.setGeometry(QRect(100, 240, 82, 26))
        self.group_hobbies = QGroupBox(self.centralwidget)
        self.group_hobbies.setObjectName(u"group_hobbies")
        self.group_hobbies.setGeometry(QRect(60, 10, 161, 221))
        self.widget = QWidget(self.group_hobbies)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 70, 77, 86))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_movies = QCheckBox(self.widget)
        self.cb_movies.setObjectName(u"cb_movies")

        self.verticalLayout.addWidget(self.cb_movies)

        self.cb_reading = QCheckBox(self.widget)
        self.cb_reading.setObjectName(u"cb_reading")

        self.verticalLayout.addWidget(self.cb_reading)

        self.cb_sports = QCheckBox(self.widget)
        self.cb_sports.setObjectName(u"cb_sports")

        self.verticalLayout.addWidget(self.cb_sports)

        self.group_lectures = QGroupBox(self.centralwidget)
        self.group_lectures.setObjectName(u"group_lectures")
        self.group_lectures.setGeometry(QRect(330, 10, 161, 221))
        self.layoutWidget = QWidget(self.group_lectures)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 70, 107, 86))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cb_web_design = QCheckBox(self.layoutWidget)
        self.cb_web_design.setObjectName(u"cb_web_design")

        self.verticalLayout_2.addWidget(self.cb_web_design)

        self.cb_programming = QCheckBox(self.layoutWidget)
        self.cb_programming.setObjectName(u"cb_programming")

        self.verticalLayout_2.addWidget(self.cb_programming)

        self.cb_math = QCheckBox(self.layoutWidget)
        self.cb_math.setObjectName(u"cb_math")

        self.verticalLayout_2.addWidget(self.cb_math)

        self.btn_get_lectures = QPushButton(self.centralwidget)
        self.btn_get_lectures.setObjectName(u"btn_get_lectures")
        self.btn_get_lectures.setGeometry(QRect(370, 240, 82, 26))
        self.lbl_result_lectures = QLabel(self.centralwidget)
        self.lbl_result_lectures.setObjectName(u"lbl_result_lectures")
        self.lbl_result_lectures.setGeometry(QRect(330, 270, 161, 121))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_result_hobbies.setText(QCoreApplication.translate("MainWindow", u"Hobbies", None))
        self.btn_get_hobbies.setText(QCoreApplication.translate("MainWindow", u"Get Hobbies", None))
        self.group_hobbies.setTitle(QCoreApplication.translate("MainWindow", u"Hobbies", None))
        self.cb_movies.setText(QCoreApplication.translate("MainWindow", u"Movies", None))
        self.cb_reading.setText(QCoreApplication.translate("MainWindow", u"Reading", None))
        self.cb_sports.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.group_lectures.setTitle(QCoreApplication.translate("MainWindow", u"Lectures", None))
        self.cb_web_design.setText(QCoreApplication.translate("MainWindow", u"Web Design", None))
        self.cb_programming.setText(QCoreApplication.translate("MainWindow", u"Programming", None))
        self.cb_math.setText(QCoreApplication.translate("MainWindow", u"Math", None))
        self.btn_get_lectures.setText(QCoreApplication.translate("MainWindow", u"Get Lectures", None))
        self.lbl_result_lectures.setText(QCoreApplication.translate("MainWindow", u"Lectures", None))
    # retranslateUi

