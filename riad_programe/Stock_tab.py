from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QDialog, QHBoxLayout, QHeaderView, QLineEdit, QVBoxLayout, QDateEdit, QTableWidget, QTableWidgetItem, QFrame , QTabWidget
from creation_database import list_produits,ajouter_produit

class StockTab(QWidget):
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
        table1.setColumnCount(4)
        table1.setRowCount(0)

        # Set table headers
        table1.setHorizontalHeaderLabels(['ID', 'Produit', 'Initial Unite price', 'Quantity'])
        horizontal_header = table1.horizontalHeader()
        for i in range(table1.columnCount()):
              horizontal_header.setSectionResizeMode(i, QHeaderView.Stretch)

        # fill the table from data base
        cursor =list_produits()
        rows = cursor.fetchall()
        num_rows = len(rows)
        table1.setRowCount(num_rows)
        row_nb=0

        cursor = list_produits()
        for row in cursor:
            id = row[0]
            prod = row[1]
            qte = row[2]
            init_prix = row[3]

            table1.setItem(row_nb, 0, QTableWidgetItem(id))
            table1.setItem(row_nb, 1, QTableWidgetItem(str(prod)))
            table1.setItem(row_nb, 2, QTableWidgetItem(str(init_prix)))
            table1.setItem(row_nb, 3, QTableWidgetItem(str(qte)))
            row_nb += 1



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
        add_button_stock.clicked.connect(self.add_new_product)
        delete_button_stock.clicked.connect(self.delete_data_from_table)


    def add_new_product(self):
            # Create a QDialog for adding data
        add_dialog = QDialog(self)
        add_dialog.setWindowTitle("Add Data")
        add_dialog.setGeometry(100, 100, 400, 200)

        # Create QLineEdit widgets for input fields
        id_edit = QLineEdit()
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
                qantite = int(quantity_edit.text())
                prix_init = int(unite_price_edit.text())
                # moh afficherlna message si had les champs sont pas de nombre ------------------------------------------------------------------------
                ajouter_produit(produit_edit.text(),qantite,prix_init)




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
