import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHeaderView, QLabel, QHBoxLayout, QWidget, QTabWidget, QVBoxLayout, QDateEdit, QLineEdit, QTableWidget, QTableWidgetItem, QFrame
from PyQt5 import QtCore, QtGui, QtWidgets
from Stock_tab import StockTab
from Employer_tab import EmployerTab
from fabrication_tab import FabricationTab
# from clients_tab import ClientsTab
# from stat_tab import StatTab



class MyWindow(QMainWindow):
    opened_tabs = []
    def __init__(self):
        super().__init__()

        # Create the horizontal layout for buttons
        buttons_layout = QHBoxLayout()

        # Create 5 push buttons with labels
        labels = ["Stock", "Employer", "Fabrication", "Clients", "Stat"]
        for label in labels:
            button = QPushButton(label)
            buttons_layout.addWidget(button)
            # Connect the buttons to their respective tabs
            if label == "Stock":
                button.clicked.connect(self.show_stock_tab)
            elif label == "Employer":
                button.clicked.connect(self.show_employer_tab)
            elif label == "Fabrication":
                button.clicked.connect(self.show_fabrication_tab)
            # elif label == "Clients":
            #     button.clicked.connect(self.show_clients_tab)
            # elif label == "Stat":
            #     button.clicked.connect(self.show_stat_tab)

        # Create a widget to hold the buttons layout
        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons_layout)

        # Create a frame for the buttons widget
        frame_buttons = QFrame()
        frame_buttons.setFrameShape(QFrame.Panel)
        frame_buttons.setFrameShadow(QFrame.Raised)
        frame_buttons.setLineWidth(2)
        frame_buttons.setLayout(QVBoxLayout())
        frame_buttons.layout().addWidget(buttons_widget)

        # Create a tab widget
        self.tab_widget = QTabWidget()
        self.tab1_widget = QTabWidget()
        central_widget = QWidget()  # New central widget
        central_layout = QVBoxLayout()  # New vertical layout for central widget
        central_layout.addWidget(self.tab_widget)  # Add tab_widget to central layout
        central_layout.addWidget(self.tab1_widget)  # Add tab1_widget to central layout
        self.tab_widget.setFixedHeight(100)
        self.tab_widget.tabBar().setVisible(False)
        central_widget.setLayout(central_layout)  # Set central layout to central widget
        self.setCentralWidget(central_widget)  # Set central widget as central widget of main window
        self.tab1_widget.setTabsClosable(True)

        self.tab1_widget.tabCloseRequested.connect(self.remove_tab)

        # Add the buttons widget to the tab widget
        self.tab_widget.addTab(frame_buttons, "Menu")


        # Set window properties
        self.setWindowTitle("Atelier Riad")

    def show_stock_tab(self, tab1_widget):
        if "Stock" not in self.opened_tabs:
            stock_tab = StockTab(tab1_widget)
            stock_tab_widget = QWidget()
            stock_tab_widget.setLayout(QVBoxLayout())
            stock_tab_widget.layout().addWidget(stock_tab)
            self.tab1_widget.addTab(stock_tab_widget, "Stock")
            self.opened_tabs.append("Stock")
            self.tab1_widget.setCurrentWidget(stock_tab_widget)
        else:
            self.tab1_widget.setCurrentIndex(self.opened_tabs.index("Stock"))
    def show_employer_tab(self, tab1_widget):
        if "Employer" not in self.opened_tabs:
            employer_tab = EmployerTab()
            employer_tab_widget = QWidget()
            employer_tab_widget.setLayout(QVBoxLayout())
            employer_tab_widget.layout().addWidget(employer_tab)
            self.tab1_widget.addTab(employer_tab_widget, "Employer")
            self.opened_tabs.append("Employer")
            self.tab1_widget.setCurrentWidget(employer_tab_widget)
        else:
            self.tab1_widget.setCurrentIndex(self.opened_tabs.index("Employer"))

    def show_fabrication_tab(self, tab1_widget):
        if "Fabrication" not in self.opened_tabs:
            fabrication_tab = FabricationTab(tab1_widget)
            fabrication_tab_widget = QWidget()
            fabrication_tab_widget.setLayout(QVBoxLayout())
            fabrication_tab_widget.layout().addWidget(fabrication_tab)
            self.tab1_widget.addTab(fabrication_tab_widget, "Fabrication")
            self.opened_tabs.append("Fabrication")
            self.tab1_widget.setCurrentWidget(fabrication_tab_widget)
        else:
            self.tab1_widget.setCurrentIndex(self.opened_tabs.index("Fabrication"))

    

    

    

    def remove_tab(self, index):
    # Get the tab text at the given index
        tab_text = self.tab1_widget.tabText(index)
    # Check if the tab text exists in opened_tabs list
        if tab_text in self.opened_tabs:
        # Remove the tab text from the opened_tabs list
            self.opened_tabs.remove(tab_text)
        # Remove the tab at the given index
            self.tab1_widget.removeTab(index)
stylesheet = """
    QMainWindow {
        background-color: #e6f5ff;
    }

    QPushButton {
        background-color: #c5e1ff;
        border-style: solid;
        border-width: 2px;
        border-radius: 10px;
        border-color: #005ce6;
        font-size: 16px;
        font-weight: bold;
        padding: 6px;
    }

    QPushButton:hover {
        background-color: #005ce6;
        color: white;
    }

    QTabWidget::tab-bar {
        alignment: center;
    }

    QTabBar::tab {
        background-color: #c5e1ff;
        color: #005ce6;
        border: 2px solid #005ce6;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        min-width: 100px;
        padding: 6px;
    }

    QTabBar::tab:selected {
        background-color: white;
        border-bottom-color: white;
    }

    QTableWidget {
        alternate-background-color: #f2f2f2;
        border-style: solid;
        border-width: 2px;
        border-radius: 10px;
        border-color: #005ce6;
    }

    QHeaderView::section {
        background-color: #c5e1ff;
        color: #005ce6;
        font-size: 14px;
        font-weight: bold;
        padding: 6px;
        border: none;
    }

    QHeaderView::section:checked {
        background-color: white;
        border-bottom-color: white;
    }

    QHeaderView {
        border: none;
    }
"""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setStyleSheet(stylesheet)
    window.showMaximized()
    sys.exit(app.exec_())
