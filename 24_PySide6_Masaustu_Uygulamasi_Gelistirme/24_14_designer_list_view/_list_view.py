"""List View Kullanımı -> Load, Add, Edit, Remove, Up-Down, Sort"""

import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QInputDialog  # Add için
from PySide6.QtWidgets import QLineEdit  # Edit için
from PySide6.QtWidgets import QMessageBox  # Remove için

from list_view_design import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Students
        self.load_students()

        # Add New Student
        self.ui.btn_add.clicked.connect(self.add_student)

        # Edit Student
        self.ui.btn_edit.clicked.connect(self.edit_student)

        # Remove Student
        self.ui.btn_remove.clicked.connect(self.remove_student)

        # Up
        self.ui.btn_up.clicked.connect(self.up)

        # Down
        self.ui.btn_down.clicked.connect(self.down)

        # Sort
        self.ui.btn_sort.clicked.connect(self.sort_students)

        # Exit
        self.ui.btn_exit.clicked.connect(self.exiting)

    def load_students(self):
        self.ui.list_items.addItems(["Utku", "Mert", "Denizhan"])
        self.ui.list_items.setCurrentRow(0)  # Default seçim

    def add_student(self):
        current_index = self.ui.list_items.currentRow()
        text, ok = QInputDialog.getText(self, "New Student", "Student Name")
        if ok and text.strip():
            self.ui.list_items.insertItem(current_index, text.strip())

    def edit_student(self):
        index = self.ui.list_items.currentRow()
        item = self.ui.list_items.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(
                self, "Edit Student", "Student Name", QLineEdit.Normal, item.text()
            )
            if ok and text.strip():
                item.setText(text.strip())

    def remove_student(self):
        index = self.ui.list_items.currentRow()
        item = self.ui.list_items.item(index)
        if item is not None:
            q = QMessageBox.question(
                self,
                "Remove Student",
                f"Do you really want to remove the student? - {item.text()}",
                QMessageBox.Yes | QMessageBox.No,
            )
            if q == QMessageBox.Yes:
                item = self.ui.list_items.takeItem(index)
                del item

    def up(self):
        index = self.ui.list_items.currentRow()
        if index > 0:
            item = self.ui.list_items.takeItem(index)
            self.ui.list_items.insertItem(index - 1, item)
            self.ui.list_items.setCurrentItem(item)

    def down(self):
        index = self.ui.list_items.currentRow()
        if index < self.ui.list_items.count() - 1:
            item = self.ui.list_items.takeItem(index)
            self.ui.list_items.insertItem(index + 1, item)
            self.ui.list_items.setCurrentItem(item)

    def sort_students(self):
        self.ui.list_items.sortItems()

    def exiting(self):
        q = QMessageBox.question(
            self,
            "Exit?",
            "Do you really want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,  # Default seçim
        )
        if q == QMessageBox.Yes:
            QtWidgets.QApplication.quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
