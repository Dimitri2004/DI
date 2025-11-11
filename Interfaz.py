import sys
import modeloLista
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QGridLayout, QListWidget)

class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primera ventana con QT")
        maia = QGridLayout()


        listaFollas=[["Follas 1","F"],["Follas 2","F"],["Follas3","F"],["Folla 4","F"],["Folla 5","D"]]
        self.modeloListaVisibles = modeloLista.ModeloFollas(listaFollas)
        self.modeloListaOcultos =modeloLista.ModeloFollas()


        lblFollasVisibles = QLabel("Follas Visibles")
        lblFollasOcultas = QLabel("Follas Ocultas")
        btnMostrar = QPushButton("<<Mostrar")
        btnMostrar.clicked.connect(self.on_btnMostrar_clicked)
        btnOcultar = QPushButton("Ocultar>>")
        btnOcultar.clicked.connect(self.on_btnOcultar_clicked)
        btnCerrar = QPushButton("Cerrar")
        btnCerrar.clicked.connect(self.on_btnCerrar_clicked)
        btnCerrar.setFixedSize(200,50)


        self.lstOculta = QListView()
        self.lstVisible = QListView()
        self.lstVisible.setModel(self.modeloListaVisibles)
        self.lstOculta.setModel(self.modeloListaOcultos)

        maia.addWidget(lblFollasVisibles)
        maia.addWidget(lblFollasOcultas,0,2,1,1)
        maia.addWidget(self.lstVisible,1,0,5,1)
        maia.addWidget(self.lstOculta,1,2,5,1)
        maia.addWidget(btnOcultar,1,1,1,1)
        maia.addWidget(btnMostrar,3,1,1,1)
        maia.addWidget(btnCerrar,7,2,1,1, alignment=Qt.AlignmentFlag.AlignRight)

        aux = QWidget()
        aux.setLayout(maia)
        aux.setFixedSize(900,600)
        self.setCentralWidget(aux)
        self.show()
    def on_btnMostrar_clicked(self):
        indices =self.lstOculta.selectedIndexes()
        if indices:
            self.modeloListaVisibles.follas.append(self.modeloListaOcultos.follas[indices[0].row()]) #coges elemento seleccionado
            del self.modeloListaOcultos.follas[indices[0].row()]
            self.modeloListaVisibles.layoutChanged.emit()
            self.modeloListaOcultos.layoutChanged.emit()
            self.lstOculta.clearSelection()


    def on_btnOcultar_clicked(self):
        indices = self.lstVisible.selectedIndexes()
        if indices:
            self.modeloListaOcultos.follas.append(self.modeloListaVisibles.follas[indices[0].row()])
            del self.modeloListaVisibles.follas[indices[0].row()]
            self.modeloListaVisibles.layoutChanged.emit()
            self.modeloListaOcultos.layoutChanged.emit()
            self.lstVisible.clearSelection()

    def on_btnCerrar_clicked(self):
        self.close()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()