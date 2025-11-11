import sys

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QGridLayout, QLabel, \
    QComboBox, QPushButton, QListView, QLineEdit, QLineEdit, QComboBox, QTextEdit, QRadioButton, QButtonGroup, \
    QTableView, QTabWidget

from ModeloTabla import ModeloTabla

class EjemploListasIntercambiables(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplos")
        maia=QGridLayout()

        datos= [['Nome','Dni','Genero', 'Fallecido'],["Ana","3356J","Muller",False],["Pepe","9865T","Home",True]]

        self.nome_dni=[['Ana','Pepe','Juan'],['7766M','5567R','9980Y']]


        caixaV=QVBoxLayout()
        rbtBoton1=QRadioButton("Boton1",self)
        rbtBoton2 = QRadioButton("Boton2", self)
        rbtBoton3 = QRadioButton("Boton3", self)
        rbtBoton4 = QRadioButton("Boton4", self)

        caixaV.addWidget(rbtBoton1)
        caixaV.addWidget(rbtBoton2)
        caixaV.addWidget(rbtBoton3)
        caixaV.addWidget(rbtBoton4)


        grupo1=QButtonGroup()
        grupo2=QButtonGroup()
        grupo1.addButton(rbtBoton1)
        grupo1.addButton(rbtBoton3)
        grupo2.addButton(rbtBoton2)
        grupo2.addButton(rbtBoton4)

        clasificador = QTabWidget()
        clasificador.setTabPosition(QTabWidget.TabPosition.North)
        maia.addWidget(clasificador, 0, 1, 1, 1)


        self.tvwTaboa=QTableView()
        self.modelo = ModeloTabla(datos)
        self.tvwTaboa.setModel(self.modelo)
        clasificador.addTab(self.tvwTaboa,"Taboa")
        txtOutroCadroTexto=QTextEdit()
        clasificador.addTab(txtOutroCadroTexto,"Cadro Texto")



        txtCadro1=QLineEdit()
        txtCadro2=QLineEdit()

        self.cmbComboBox=QComboBox()
        self.cmbComboBox.addItems(self.nome_dni[0])
        self.cmbComboBox.currentIndexChanged.connect(self.on_cmbComboBox_currentIndexChanged)
        self.cmbComboBox.currentTextChanged.connect(self.on_cmbComboBox_currentTextChanged)

        caixaV.addWidget(txtCadro1)
        caixaV.addWidget(txtCadro2)
        caixaV.addWidget(self.cmbComboBox)
        maia.addLayout(caixaV,1,0,1,1)

        self.txtAreaTexto=QTextEdit()
        maia.addWidget(self.txtAreaTexto,1,1,1,1)

        aux =QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)

    def on_cmbComboBox_currentIndexChanged(self,indice):
        print(self.cmbComboBox.currentText())
        self.txtAreaTexto.setPlainText("Seleccionaste el elemento "+ self.cmbComboBox.itemText(indice)+ " con dni: "+self.nome_dni[1][indice])

    def on_cmbComboBox_currentTextChanged(self, texto):
        print("O combo ten seleccionado o texto: "+texto)


if __name__ == "__main__":
    aplicaccion=QApplication(sys.argv)
    window=EjemploListasIntercambiables()
    window.show()
    sys.exit(aplicaccion.exec())




