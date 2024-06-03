import mysql.connector
import random 

class modelo: 
    def __init__(self, nombre, definicion, enfermedad, sintomas, especialista, tratamiento, ID, id_enfermedad ):
        self.__login = "admin123"
        self.__password = "contrasena123"
        self.__ID = ID
        self.__id_enfermedad = id_enfermedad
        self.__parte_del_cerebro = nombre
        self.__definicion = definicion
        self.__enfermedad = enfermedad
        self.__sintomas = sintomas
        self.__especialista = especialista
        self.__tratamiento = tratamiento

        self.__cnx = mysql.connector.connect(
            user='admin123', password='contrasena123', host='localhost', database='info_2'
        )
        self.__cursor = self.__cnx.cursor() 
    
    def setlogin(self, admin123):
        self.__login = admin123

    def setPassword(self, contrasena123):
        self.__password = contrasena123

    def Validar_usuario(self, admin123, contrasena123):
        if (self.__login == admin123) and (self.__password == contrasena123):
            return "BIENVENID@"
        else:
            return "USUARIO INVALIDO"
    
    def extraer_info(self,id_):
        sql = "select * from general  where ID="+str(id_)   
        self.__cursor.execute(sql)
        results = self.__cursor.fetchall()
        return results

    def pregunta(self):
       preguntas = [
        "¿Cuál es el lóbulo encargado de los procesos cognitivos complejos?",
        "¿Cuál es el lóbulo relacionado con el funcionamiento de lenguaje?",
        "¿Parte de la corteza cerebral encargada de la fluidez del movimiento?",
        "¿Parte de la corteza cerebral que transmite la emergencia motora del lenguaje?",
        "Lóbulo ubicado en la parte posterior del cerebro ...",
        "¿Cuál es el lóbulo crucial para la interpretación visual del humano?",
        "Interpreta cuando el ser humano siente dolor, frío, calor ...",
        "Lóbulo ubicado cerca de las sienes ...",
        "Esencial en la audición humana, su daño afecta la calidad de vida ...",
        "Lóbulo asociado con el sentido olfativo ..."] 
       preguntas_aleatorias = random.sample(preguntas,4)
       return preguntas_aleatorias
    
    def ID(self):
        return self.__ID
    
    def id_enfermedad(self):
        return self.__id_enfermedad
    
    def nombre(self):
        return self.__parte_del_cerebro
    
    def definicion(self):
        return self.__definicion
    
    def enfermedad(self):
        return self.__enfermedad
    
    def sintomas(self):
        return self.__sintomas
    
    def especialista(self):
        return self.__especialista
    
    def tratamiento(self):
        return self.__tratamiento
    

    

