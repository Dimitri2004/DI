import PyQt6.QtWidgets
from PyQt6.QtCore import Qt
import sys

from PyQt6.QtGui import QAction


class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WindowTitle")



        # === TOOL BAR ===
        toolbar = PyQt6.QtWidgets.QToolBar()
        self.addToolBar(toolbar)

        toolbar_button = QAction("ToolbarButton", self)
        toolbar.addAction(toolbar_button)

        toolbar_checkbox = PyQt6.QtWidgets.QCheckBox("ToolbarCheckBox")
        toolbar.addWidget(toolbar_checkbox)

        # === CENTRAL WIDGET ===
        central_widget = PyQt6.QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        main_layout = PyQt6.QtWidgets.QVBoxLayout()
        central_widget.setLayout(main_layout)

        # --- Panel Caption ---
        panel_caption = PyQt6.QtWidgets.QLabel("PanelCaption")
        main_layout.addWidget(panel_caption)

        # --- Panel Layout ---
        panel_layout = PyQt6.QtWidgets.QGridLayout()
        main_layout.addLayout(panel_layout)

        # === Left side: List + Radio Buttons + Button ===
        left_layout = PyQt6.QtWidgets.QVBoxLayout()

        # List
        self.list_widget = PyQt6.QtWidgets.QListWidget()
        for i in range(1, 6):
            self.list_widget.addItem(f"Item {i}")
        left_layout.addWidget(self.list_widget)

        # Radio buttons
        radio_group = PyQt6.QtWidgets.QGroupBox()
        radio_layout = PyQt6.QtWidgets.QVBoxLayout()
        radio_group.setLayout(radio_layout)
        radios = [
            PyQt6.QtWidgets.QRadioButton("RadioButton1"),
            PyQt6.QtWidgets.QRadioButton("RadioButton2"),
            PyQt6.QtWidgets.QRadioButton("RadioButton3"),
            PyQt6.QtWidgets.QRadioButton("InactiveRadio")
        ]
        radios[-1].setEnabled(False)
        radios[0].setChecked(True)
        for r in radios:
            radio_layout.addWidget(r)
        left_layout.addWidget(radio_group)

        # Button
        button = PyQt6.QtWidgets.QPushButton("Button")
        left_layout.addWidget(button)

        panel_layout.addLayout(left_layout, 0, 0)

        # === Right side: Tabs ===
        tabs = PyQt6.QtWidgets.QTabWidget()
        selected_tab = PyQt6.QtWidgets.QWidget()
        tab_layout = PyQt6.QtWidgets.QVBoxLayout()
        selected_tab.setLayout(tab_layout)

        check1 = PyQt6.QtWidgets.QCheckBox("UncheckedCheckBox")
        check2 = PyQt6.QtWidgets.QCheckBox("CheckedCheckBox")
        check2.setChecked(True)
        check3 = PyQt6.QtWidgets.QCheckBox("InactiveCheckBox")
        check3.setEnabled(False)
        for c in [check1, check2, check3]:
            tab_layout.addWidget(c)

        slider = PyQt6.QtWidgets.QSlider(Qt.Orientation.Horizontal)
        tab_layout.addWidget(slider)

        tabs.addTab(selected_tab, "SelectedTab")
        tabs.addTab(PyQt6.QtWidgets.QWidget(), "OtherTab")

        panel_layout.addWidget(tabs, 0, 1)

        # === Bottom section: Text Fields ===
        bottom_layout = PyQt6.QtWidgets.QGridLayout()
        main_layout.addLayout(bottom_layout)

        text_field = PyQt6.QtWidgets.QLineEdit()
        text_field.setPlaceholderText("TextField")
        text_field.setEchoMode(PyQt6.QtWidgets.QLineEdit.EchoMode.Password)
        bottom_layout.addWidget(text_field, 0, 0)

        text_area = PyQt6.QtWidgets.QTextEdit()
        text_area.setPlaceholderText("TextArea")
        bottom_layout.addWidget(text_area, 0, 1)

        combo = PyQt6.QtWidgets.QComboBox()
        combo.addItems([f"Item {i}" for i in range(1, 6)])
        bottom_layout.addWidget(combo, 1, 0)


if __name__ == "__main__":
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())
