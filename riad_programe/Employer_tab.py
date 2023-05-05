from PyQt5.QtWidgets import QWidget, QPushButton, QDateEdit, QTableWidget, QTableWidgetItem, QFrame, QVBoxLayout, QHBoxLayout


class EmployerTab(QWidget):
    def __init__(self):
        super().__init__()

        # Create "Add" and "Delete" push buttons
        add_button = QPushButton("Add")
        delete_button = QPushButton("Delete")
        date_button = QDateEdit()
        close_button = QPushButton("Close")

        # Create a QTableWidget
        table2 = QTableWidget()
        table2.setColumnCount(2)
        table2.setRowCount(3)

        # Set table headers
        table2.setHorizontalHeaderLabels(['Column 1', 'Column 2'])

        # Set table data
        for row in range(3):
            for col in range(2):
                item = QTableWidgetItem(f'Row {row+1}, Col {col+1}')
                table2.setItem(row, col, item)

        # Add the buttons to a horizontal frame
        frame2 = QFrame()
        frame2.setFrameShape(QFrame.Box)
        frame2.setLineWidth(1)
        frame2_layout = QHBoxLayout()
        frame2_layout.addWidget(add_button)
        frame2_layout.addWidget(delete_button)
        frame2_layout.addWidget(date_button)
        frame2_layout.addWidget(close_button)
        frame2.setLayout(frame2_layout)

        # Add the frame and table widget to the layout
        layout = QVBoxLayout()
        layout.addWidget(frame2)
        layout.addWidget(table2)

        self.setLayout(layout)
