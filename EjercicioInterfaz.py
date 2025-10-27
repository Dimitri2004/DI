from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QGridLayout, QListView, \
    QCheckBox, QPushButton, QLabel


class EjercicioInterfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXCELeINFO-HOJAS")

        caixaH=QHBoxLayout()
        caixaV=QVBoxLayout()

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)


        #Wiguet de la izquierda
        left_layout = QVBoxLayout()
        self.label1=QLabel("Hojas visibles")
        self.box1=QListView()
        left_layout.addWidget(self.label1)
        left_layout.addWidget(self.box1)
        caixaH.addLayout(left_layout)

        #Wiguet central
        central_layout=QVBoxLayout()
        self.boton2=QPushButton("<<Mostrar")
        self.boton1=QPushButton("Ocultar>>")
        central_layout.addWidget(self.boton1)
        central_layout.addWidget(self.boton2)
        caixaH.addLayout(central_layout)

        #Wiguet de la derecha
        right_layout = QVBoxLayout()
        self.label2 = QLabel("Hojas Ocultas")
        self.box2=QListView()
        self.boton3=QPushButton("Cerrar")
        self.boton3.setFixedSize(100,40)

        right_layout.addWidget(self.label2)
        right_layout.addWidget(self.box2)
        right_layout.addWidget(self.boton3, alignment=Qt.AlignmentFlag.AlignHCenter)
        caixaH.addLayout(right_layout)



        main_layout.addLayout(caixaH)
        main_layout.addLayout(caixaV)



        self.show()
if __name__ == "__main__":
    app = QApplication([])
    window = EjercicioInterfaz()
    app.exec()