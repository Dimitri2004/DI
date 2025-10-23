from PyQt6.QtGui import QPalette, QColor

import controles

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication,QWidget

from controles import CaixaCor

class Box(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo Ventana Colores")


        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Left column
        left_layout = QVBoxLayout()
        left_layout.addWidget(CaixaCor("red"))
        left_layout.addWidget(CaixaCor("yellow"))
        left_layout.addWidget(CaixaCor("red"))

        # Center column
        center_layout = QVBoxLayout()
        center_layout.addWidget(CaixaCor("red"))
        center_layout.addWidget(CaixaCor("yellow"))
        center_layout.addWidget(CaixaCor("red"))

        # Right column
        right_layout = QVBoxLayout()
        right_layout.addWidget(CaixaCor("red"))
        right_layout.addWidget(CaixaCor("yellow"))
        right_layout.addWidget(CaixaCor("red"))
        # Add columns to main layout
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = Box()
    app.exec()



