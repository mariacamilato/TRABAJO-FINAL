import mysql.connector
import random 
class modelo: 
    enfermedades = []
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
    
    def agregar_enfermedad(self, nombre, sintomas, especialista,tratamiento, id_enfermedad):
        if not self.verificar_existencia(id_enfermedad):
            enfermedad = (nombre, sintomas, especialista,tratamiento, id_enfermedad)
            self.enfermedades.append(enfermedad)
            self.guardar__enfermedad("enfermedades.json")
            return True
        else: 
             return False
    
    def verificar_existencia(self, id_enfermedad):
        for enfermedad in self.pacientes:
            if enfermedad[3] == id_enfermedad:
                return True
        return False
    
    def guardar_enfermedad(self, archivo):
       enfermedad_json = [
           {
               "nombre" : enfermedad[0],
               "apellido": enfermedad[1],
               "edad": enfermedad[2],
               "ID" : enfermedad[3]
           }
           for enfermedad in self.enferdad
       ]
       with open(archivo, 'w') as f:
           json.dump(enfermedad_json, f, indent=2)
    
    def cargar_pacientes_desde_archivo(self, archivo):
        self.pacientes = []
        with open(archivo, 'r') as f:
            pacientes_json = json.load(f)

            for paciente_json in pacientes_json:
                paciente = (
                    paciente_json["nombre"],
                    paciente_json["apellido"],
                    paciente_json["edad"],
                    paciente_json["ID"]
                )
                self.pacientes.append(paciente)
    

    

