from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap 

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("untitled.ui",self)
        self.setup()
    
    def setup(self):
        self.pushButton.clicked.connect(self.ingresar)
    
    def ingresar(self):
        usuario=self.campo_usuario.text()
        contraseña=self.campo_contraseña.text()
        print(f"El usuario ingresado es {usuario} y su contraseña {contraseña}")
