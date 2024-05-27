import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OFDMA downlink simulation")
        self.setGeometry(100, 100, 1000, 600)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Time Slot', 'Frequency Subcarrier', 'User ID', 'Packet Data'])

        self.param_layout = QVBoxLayout()
        self.param_layout.addWidget(QLabel("New Column Name:"))
        self.column_name_input = QLineEdit()
        self.param_layout.addWidget(self.column_name_input)
        self.add_column_button = QPushButton("Add Column")
        self.add_column_button.clicked.connect(self.add_column)
        self.param_layout.addWidget(self.add_column_button)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.param_layout)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.populate_table()

    def populate_table(self):
        data = [
            [1, 'Subcarrier 1', 'User A', 'Packet 1'],
            [1, 'Subcarrier 2', 'User B', 'Packet 2'],
            [2, 'Subcarrier 1', 'User C', 'Packet 3'],
            [2, 'Subcarrier 2', 'User A', 'Packet 4']
        ]

        self.table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(0x0004)  # Align text horizontally to the right
                self.table.setItem(i, j, item)

    def add_column(self):
        new_column_name = self.column_name_input.text()
        self.table.setColumnCount(self.table.columnCount() + 1)
        self.table.setHorizontalHeaderItem(self.table.columnCount() - 1, QTableWidgetItem(new_column_name))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
