import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)


#QVBoxLayout - añade controles en vertical
#QHBoxLayout - añade controles en horizontal

class NuestraPrimeraVentana (QMainWindow):

    def on_btnSaludo_clicked(self):
        nome = self.txtSaludo.text()
        nome= nome.strip()
        self.txtSaludo.clear()
        self.txtSaludo.setText("")
        self.lblEtiqueta.setText("Hola "+ nome)

    #boton que cree otra ventana y que al volver a pulsar returne a la principal

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera Ventana con QT")
        self.setMinimumSize(500,300)

        self.txtSaludo = QLineEdit()

        self.lblEtiqueta = QLabel("Hola a todos")

        self.txtSaludo= QLineEdit()
        self.txtSaludo.setPlaceholderText("Introduce o teu nome")
        self.txtSaludo.returnPressed.connect(self.on_btnSaludo_clicked)

        fuente = self.lblEtiqueta.font()
        fuente.setPointSize(30)
        self.lblEtiqueta.setFont(fuente)

        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter| Qt.AlignmentFlag.AlignVCenter)



        btnSaludo = QPushButton("Saludo")

        btnSaludo.clicked.connect(self.on_btnSaludo_clicked)

        caixaV=QVBoxLayout()

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaludo)
        caixaV.addWidget(btnSaludo)

        container = QWidget()
        container.setLayout(caixaV)


        self.setCentralWidget(container)
        self.show()
        #self.hide() esconde ventana

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana= NuestraPrimeraVentana()
    aplicacion.exec()



