from Modelo import modelo
from Vista import *
from PyQt5.QtWidgets import QApplication
import sys 

class Coordinador:
    def __init__(self,vista,modelo):
        self.__miVista = vista
        self.__miModelo = modelo
    
    def validar(self,usuario,contraseña):
        resultado=self.__miModelo.Validar_usuario(usuario,contraseña)
        self.__miVista.mensaje(resultado)
        return resultado 
    
    def extraer_info(self,id):
        resultado=self.__miModelo.extraer_info(id)
        return resultado
    
    def preguntaLanzar(self):
        preguntas=self.__miModelo.pregunta()
        return preguntas
    
    def ingresarInfo(self,a,b,c,d,e):
        resultado=self.__miModelo.agregar_enfermedad(a,b,c,d,e)
        return resultado
    
    def buscarEnfermedad(self,nombre):
        resultado=self.__miModelo.buscar_enfermedad(nombre)
        return resultado
    
    def borrarEnfermedad(self,ide):
        resultado=self.__miModelo.borrar_enfermedad(ide)
        return resultado
    
    def binarizar(self,ruta):
        resultado=self.__miModelo.BinarizarImagen(ruta)
        return resultado 

def main():
    app=QApplication(sys.argv)
    vista=Login()
    modelo_instancia=modelo("e","e","e","e","e")
    coordinador= Coordinador(vista,modelo_instancia)
    vista.set_coordinador(coordinador)
    vista.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()