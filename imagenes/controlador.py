from vista import VentanaLogin
from modelo import BaseDatos
import sys 
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtGui import QPixmap 

class Coordinador:
    def __init__(self,vista,modelo):
        self.__vista= vista
        self.__modelo=modelo

def main():
    app=QApplication(sys.argv)
    vista=VentanaLogin()
    modelo=BaseDatos()
    coordinador= Coordinador(vista,modelo)
    vista.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()