import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout)
#QVBoxLayout - añade controles en vertical
#QHBoxLayout - añade controles en horizontal

class NuestraPrimeraVentana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera Ventana con QT")
        self.setMinimumSize(500,300)


        self.txtSaludo = QLineEdit()

        self.lblEtiqueta = QLabel("Hola a todos")

        fuente = self.lblEtiqueta.font()
        fuente.setPointSize(30)
        self.lblEtiqueta.setFont(fuente)

        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter| Qt.AlignmentFlag.AlignVCenter)



        self.show()
        #self.hide() esconde ventana

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana= NuestraPrimeraVentana()
    aplicacion.exec()



