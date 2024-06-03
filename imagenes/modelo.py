class BaseDatos:
    def __init__(self):
        self.__usuario =""
        self.__contraseña =""
    
    def setUsuario(self,u):
        self.__usuario=u

    def setContraseña(self,c):
        self.__contraseña=c
    
    def validarUsuario(self,u,c):
        if self.__usuario==u and self.__contraseña==c:
            pass