import mysql.connector
import random  
class modelo: 
    def __init__(self, nombre, sintomas, especialista, tratamiento, id_enfermedad ):
        self.__login = "admin123"
        self.__password = "contrasena123"
        self.__id_enfermedad = id_enfermedad
        self.__nombre=nombre
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
    
    def id_enfermedad(self):
        return self.__id_enfermedad
    
    def nombre(self):
        return self.__nombre
    
    def sintomas(self):
        return self.__sintomas
    
    def especialista(self):
        return self.__especialista
    
    def tratamiento(self):
        return self.__tratamiento
    
    def agregar_enfermedad(self,id_enfermedad,nombre, sintomas,especialista,tratamiento):
        sql = "INSERT INTO enfermedades (id_enfermedad,nombre, sintomas, especialista, tratamiento) VALUES (%s, %s, %s, %s, %s)"
        values = (id_enfermedad,nombre,sintomas,especialista,tratamiento)
        self.__cursor.execute(sql, values)
        self.__cnx.commit()
        return "Enfermedad agregada con éxito."

    def borrar_enfermedad(self, id_enfermedad):
        sql = "DELETE FROM enfermedades WHERE id_enfermedad = %s"
        value = (id_enfermedad,)
        self.__cursor.execute(sql, value)
        self.__cnx.commit()
        return "Enfermedad borrada con éxito."

    def buscar_enfermedad(self, id_enfermedad):
        sql = "SELECT * FROM enfermedades WHERE id_enfermedad = %s"
        value = (id_enfermedad,)
        self.__cursor.execute(sql, value)
        result = self.__cursor.fetchone()
        if result:
            print("Enfermedad encontrada:", result)
        else:
            print("Enfermedad no encontrada.")
    

    

