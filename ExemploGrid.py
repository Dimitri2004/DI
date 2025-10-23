
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QGridLayout

from controles import CaixaCor

class ejemplosGrid(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo Grid")


        maia=QGridLayout()
        maia.addWidget(CaixaCor ("red"))
        maia.addWidget(CaixaCor("blue"),0,1,1,2)#coordenadas de expansion y posicion en el grid
        maia.addWidget(CaixaCor("green"), 1, 0, 2, 1)  # coordenadas de expansion y posicion en el grid
        maia.addWidget(CaixaCor("orange"), 1, 1, 1, 2)  # coordenadas de expansion y posicion en el grid
        maia.addWidget(CaixaCor("black"), 2, 1, 1, 1)  # coordenadas de expansion y posicion en el grid
        maia.addWidget(CaixaCor("yellow"), 2,2, 1, 1)  # coordenadas de expansion y posicion en el grid


        # Central widget and main layout
        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)

        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = ejemplosGrid()
    app.exec()