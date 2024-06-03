import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit,QWidget,QFileDialog,QLabel 
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QPixmap 
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLabel, QWidget
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

def pageInicio(self):
    self.stackedWidget.setCurrentIndex(0)
    self.label_animation = self.findChild(QLabel, 'label_animation')
    if self.label_animation: 
        self.movie = QMovie("9v0u.gif")
        self.label_animation.setMovie(self.movie)
        self.movie.start()
        print("Animación cargada correctamente")
    else:
        print("No se encontró el widget 'label_animation'")
    
pageInicio()


