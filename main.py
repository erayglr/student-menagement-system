from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QMainWindow, QTableWidget
import sys
from PyQt6.QtGui import QAction
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)  # baştaki self classa ref

    def load_data(self):
        self.table


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())