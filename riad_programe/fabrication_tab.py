from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QDialog, QHBoxLayout, QHeaderView, QLineEdit, QVBoxLayout, QDateEdit, QTableWidget, QTableWidgetItem, QFrame , QTabWidget


class FabricationTab(QWidget):
    def __init__(self , tab1_widget):
        super().__init__()
        self.tab1_widget = tab1_widget
        # Create "Add" and "Delete" push buttons
        add_button_stock = QPushButton("Add")
        add_button_stock.setFixedSize(100, 30)
        delete_button_stock = QPushButton("Delete")
        delete_button_stock.setFixedSize(100,30)
        changer_stock = QPushButton("changer stock")
        changer_stock.setFixedSize(120, 30)
        


        # Create a QTableWidget
        table1 = QTableWidget()
        table1.setColumnCount(5)
        table1.setRowCount(0)

        # Set table headers
        table1.setHorizontalHeaderLabels(['ID', 'Employer', 'Produit', 'Unite price', 'Quantity'])
        horizontal_header = table1.horizontalHeader()
        for i in range(table1.columnCount()):
              horizontal_header.setSectionResizeMode(i, QHeaderView.Stretch)


        # Add the buttons to a horizontal frame
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setLineWidth(1)
        frame_layout = QHBoxLayout()
        frame_layout.addWidget(add_button_stock)
        frame_layout.addWidget(delete_button_stock)
        frame_layout.addWidget(changer_stock)
        frame.setLayout(frame_layout)

        # Add the frame and table widget to the layout
        layout = QVBoxLayout()
        layout.addWidget(frame)
        layout.addWidget(table1)

        self.setLayout(layout)
        add_button_stock.clicked.connect(self.add_data_to_table)
        delete_button_stock.clicked.connect(self.delete_data_from_table)


    def add_data_to_table(self):
            # Create a QDialog for adding data
        add_dialog = QDialog(self)
        add_dialog.setWindowTitle("Add Data")
        add_dialog.setGeometry(100, 100, 400, 200)

        # Create QLineEdit widgets for input fields
        id_edit = QLineEdit()
        employer_edit = QLineEdit()
        produit_edit = QLineEdit()
        unite_price_edit = QLineEdit()
        quantity_edit = QLineEdit()

        # Create "OK" button for accepting input
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(add_dialog.accept)

        # Create layout for QDialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(QLabel("ID:"))
        dialog_layout.addWidget(id_edit)
        dialog_layout.addWidget(QLabel("Employer:"))
        dialog_layout.addWidget(employer_edit)
        dialog_layout.addWidget(QLabel("Produit:"))
        dialog_layout.addWidget(produit_edit)
        dialog_layout.addWidget(QLabel("Unit Price:"))
        dialog_layout.addWidget(unite_price_edit)
        dialog_layout.addWidget(QLabel("Quantity:"))
        dialog_layout.addWidget(quantity_edit)
        dialog_layout.addWidget(ok_button)

        add_dialog.setLayout(dialog_layout)

        # Show the QDialog as a modal window
        result = add_dialog.exec_()
        if result == QDialog.Accepted:
            table = self.findChild(QTableWidget)
            if table:
                # Get the current row count
                row_count = table.rowCount()

                # Insert a new row
                table.insertRow(row_count)

                # Add data to the new row
                table.setItem(row_count, 0, QTableWidgetItem(id_edit.text()))
                table.setItem(row_count, 1, QTableWidgetItem(employer_edit.text()))
                table.setItem(row_count, 2, QTableWidgetItem(produit_edit.text()))
                table.setItem(row_count, 3, QTableWidgetItem(unite_price_edit.text()))
                table.setItem(row_count, 4, QTableWidgetItem(quantity_edit.text()))
    def delete_data_from_table(self):
        # Get the selected row(s) from the table
        table = self.findChild(QTableWidget)
        selected_rows = table.selectedItems()
        selected_rows_set = set()
        for item in selected_rows:
            selected_rows_set.add(item.row())

        # Delete the selected row(s) from the table
        for row in sorted(selected_rows_set, reverse=True):
            table.removeRow(row)