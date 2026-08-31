# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_view_design.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 477)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.list_items = QListWidget(self.centralwidget)
        self.list_items.setObjectName(u"list_items")
        self.list_items.setGeometry(QRect(10, 30, 381, 361))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(440, 31, 151, 361))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")

        self.verticalLayout.addWidget(self.btn_edit)

        self.btn_remove = QPushButton(self.widget)
        self.btn_remove.setObjectName(u"btn_remove")

        self.verticalLayout.addWidget(self.btn_remove)

        self.btn_up = QPushButton(self.widget)
        self.btn_up.setObjectName(u"btn_up")

        self.verticalLayout.addWidget(self.btn_up)

        self.btn_down = QPushButton(self.widget)
        self.btn_down.setObjectName(u"btn_down")

        self.verticalLayout.addWidget(self.btn_down)

        self.btn_sort = QPushButton(self.widget)
        self.btn_sort.setObjectName(u"btn_sort")

        self.verticalLayout.addWidget(self.btn_sort)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_exit = QPushButton(self.widget)
        self.btn_exit.setObjectName(u"btn_exit")

        self.verticalLayout.addWidget(self.btn_exit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 627, 33))
        self.menuList_View = QMenu(self.menubar)
        self.menuList_View.setObjectName(u"menuList_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuList_View.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btn_up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.btn_down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.btn_sort.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuList_View.setTitle(QCoreApplication.translate("MainWindow", u"List View", None))
    # retranslateUi

