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

class Login(QWidget):
    def __init__(self,ppal=None, ):
        super().__init__(ppal)
        loadUi("login.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup()
       
    def setup(self):
        self.ingresar.clicked.connect(self.validar)
        self.minimizar.clicked.connect(self.minimizarVentana)
        self.salir.clicked.connect(self.salirVentana)

    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def validar(self):
        usuario=self.campo_usuario.text()
        contraseña=self.campo_contra.text()
        resultado_validacion=self.coordinador.validar(usuario,contraseña) 
        if resultado_validacion == "BIENVENID@" :
            ventanaplataforma=Plataforma(self)
            ventanaplataforma.set_coordinador(self.coordinador)
            ventanaplataforma.show() 

    def mensaje(self, message):
        if message != "BIENVENID@":
            QMessageBox.information(self, "Resultado de Login", message)
        else:
            pass
    
    def minimizarVentana(self):
        self.showMinimized()
    
    def salirVentana(self):
        self.hide()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        try:
            if self.dragging:
                self.move(self.mapToGlobal(event.pos() - self.offset))
        except:
            pass

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

class Plataforma(QMainWindow):
    def __init__(self,ppal=None, ):
        super().__init__(ppal)
        loadUi("plataforma.ui",self)
        self.setup()

    def setup(self):
        self.regresar.clicked.connect(self.abrirLogin)
        self.minimizar.clicked.connect(self.minimizarVentana)
        self.cerrar.clicked.connect(self.salirVentana)
        self.explora.clicked.connect(self.pageExplora)
        self.retate.clicked.connect(self.pageRetate)
        self.investiga.clicked.connect(self.pageInvestiga)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def abrirLogin(self):
        ventanaLogin=Login(self)
        ventanaLogin.set_coordinador(self.coordinador)
        self.hide()
        ventanaLogin.show()
    
    def minimizarVentana(self):
        self.showMinimized()
    
    def salirVentana(self):
        self.hide()
    
    def pageInicio(self):
        self.stackedWidget.setCurrentIndex(0)
        self.label_animation = self.findChild(QLabel, 'label_animation')
        if self.label_animation: 
            self.movie = QMovie("imagenes\9v0u.gif")
            self.label_animation.setMovie(self.movie)
            self.movie.start()

    def pageExplora(self):##################################
        self.stackedWidget.setCurrentIndex(1)
        self.frontal.clicked.connect(self.mostrarFrontal)
        self.parietal.clicked.connect(self.mostrarParietal)
        self.occipital.clicked.connect(self.mostrarOccipital)
        self.temporal.clicked.connect(self.mostrarTemporal)
        self.cerebelo.clicked.connect(self.mostrarCerebelo)
        self.espinal.clicked.connect(self.mostrarEspinal)
    
    def mostrarFrontal(self):
        ventana = darInfoFrontal(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        ventana.mostrar()
    
    def mostrarParietal(self):
        ventana = darInfoParietal(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        ventana.mostrar()
    
    def mostrarOccipital(self):
        ventana = darInfoOccipital(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        ventana.mostrar()
        
    def mostrarTemporal(self):
        ventana = darInfoTemporal(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        ventana.mostrar()
    
    def mostrarCerebelo(self):
        ventana = darInfoCerebelo(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        ventana.mostrar()
    
    def mostrarEspinal(self):
        ventana = darInfoEspinal(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        ventana.mostrar()
    
    def pageInvestiga(self):##################################
            self.stackedWidget.setCurrentIndex(3)
            self.agregar.clicked.connect(self.agregar_enfermedad)
            self.buscar.clicked.connect(self.buscar_enfermedad)
            self.borrar.clicked.connect(self.borrar_enfermedad )  

    def agregar_enfermedad(self):
        ventana = agregrar_E(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
    
    def buscar_enfermedad(self):
        ventana = buscar_E(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
    
    def borrar_enfermedad(self):
        ventana = borrar_E(self)
        ventana.set_coordinador(self.coordinador)
        ventana.show()
        
    def pageRetate(self):##################################
        self.stackedWidget.setCurrentIndex(2)
        pregunta = self.coordinador.preguntaLanzar()
        self.preguntarosa = pregunta[0] 
        self.preguntaamarilla=pregunta[1]
        self.preguntaverde=pregunta[2]
        self.preguntaazul=pregunta[3]
        self.pregunta1.setPlainText(str(self.preguntarosa))
        self.pregunta2.setPlainText(str(self.preguntaamarilla))
        self.pregunta3.setPlainText(str(self.preguntaverde))
        self.pregunta4.setPlainText(str(self.preguntaazul))
        self.confirmar1.clicked.connect(self.validar_respuestarosa)
        self.confirmar2.clicked.connect(self.validar_respuestaamarilla)
        self.confirmar3.clicked.connect(self.validar_respuestaverde)
        self.confirmar4.clicked.connect(self.validar_respuestaazul)
       
    def validar_respuestarosa(self):
        respuesta_usuario = self.respuesta1.text().upper()
        if self.preguntarosa == "¿Cuál es el lóbulo encargado de los procesos cognitivos complejos?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "¿Cuál es el lóbulo relacionado con el funcionamiento de lenguaje?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "¿Parte de la corteza cerebral encargada de la fluidez del movimiento?" and respuesta_usuario == "CEREBELO":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "¿Parte de la corteza cerebral que transmite la emergencia motora del lenguaje?" and respuesta_usuario == "MEDULA ESPINAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "Lóbulo ubicado en la parte posterior del cerebro ..." and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "¿Cuál es el lóbulo crucial para la interpretación visual del humano?" and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "Interpreta cuando el ser humano siente dolor, frío, calor ..." and respuesta_usuario == "LOBULO PARIETAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "Lóbulo ubicado cerca de las sienes ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "Esencial en la audición humana, su daño afecta la calidad de vida ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntarosa == "Lóbulo asociado con el sentido olfativo ..." and respuesta_usuario == "LOBULO PARIELTA":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        else:
            QMessageBox.information(self, "Resultado", "Respuesta incorrecta. Por favor, inténtalo de nuevo.")
    
    def validar_respuestaamarilla(self):
        respuesta_usuario = self.respuesta2.text().upper()
        if self.preguntaamarilla == "¿Cuál es el lóbulo encargado de los procesos cognitivos complejos?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "¿Cuál es el lóbulo relacionado con el funcionamiento de lenguaje?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "¿Parte de la corteza cerebral encargada de la fluidez del movimiento?" and respuesta_usuario == "CEREBELO":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "¿Parte de la corteza cerebral que transmite la emergencia motora del lenguaje?" and respuesta_usuario == "MEDULA ESPINAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "Lóbulo ubicado en la parte posterior del cerebro ..." and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "¿Cuál es el lóbulo crucial para la interpretación visual del humano?" and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "Interpreta cuando el ser humano siente dolor, frío, calor ..." and respuesta_usuario == "LOBULO PARIETAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "Lóbulo ubicado cerca de las sienes ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "Esencial en la audición humana, su daño afecta la calidad de vida ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaamarilla == "Lóbulo asociado con el sentido olfativo ..." and respuesta_usuario == "LOBULO PARIELTA":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        else:
            QMessageBox.information(self, "Resultado", "Respuesta incorrecta. Por favor, inténtalo de nuevo.")
    
    def validar_respuestaverde(self):
        respuesta_usuario = self.respuesta3.text().upper()
        if self.preguntaverde == "¿Cuál es el lóbulo encargado de los procesos cognitivos complejos?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "¿Cuál es el lóbulo relacionado con el funcionamiento de lenguaje?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "¿Parte de la corteza cerebral encargada de la fluidez del movimiento?" and respuesta_usuario == "CEREBELO":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "¿Parte de la corteza cerebral que transmite la emergencia motora del lenguaje?" and respuesta_usuario == "MEDULA ESPINAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "Lóbulo ubicado en la parte posterior del cerebro ..." and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "¿Cuál es el lóbulo crucial para la interpretación visual del humano?" and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "Interpreta cuando el ser humano siente dolor, frío, calor ..." and respuesta_usuario == "LOBULO PARIETAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "Lóbulo ubicado cerca de las sienes ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "Esencial en la audición humana, su daño afecta la calidad de vida ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaverde == "Lóbulo asociado con el sentido olfativo ..." and respuesta_usuario == "LOBULO PARIELTA":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        else:
            QMessageBox.information(self, "Resultado", "Respuesta incorrecta. Por favor, inténtalo de nuevo.")
    
    def validar_respuestaazul(self):
        respuesta_usuario = self.respuesta4.text().upper()
        if self.preguntaazul == "¿Cuál es el lóbulo encargado de los procesos cognitivos complejos?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "¿Cuál es el lóbulo relacionado con el funcionamiento de lenguaje?" and respuesta_usuario == "LOBULO FRONTAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "¿Parte de la corteza cerebral encargada de la fluidez del movimiento?" and respuesta_usuario == "CEREBELO":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "¿Parte de la corteza cerebral que transmite la emergencia motora del lenguaje?" and respuesta_usuario == "MEDULA ESPINAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "Lóbulo ubicado en la parte posterior del cerebro ..." and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "¿Cuál es el lóbulo crucial para la interpretación visual del humano?" and respuesta_usuario == "LOBULO OCCIPITAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "Interpreta cuando el ser humano siente dolor, frío, calor ..." and respuesta_usuario == "LOBULO PARIETAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "Lóbulo ubicado cerca de las sienes ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "Esencial en la audición humana, su daño afecta la calidad de vida ..." and respuesta_usuario == "LOBULO TEMPORAL":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        elif self.preguntaazul == "Lóbulo asociado con el sentido olfativo ..." and respuesta_usuario == "LOBULO PARIELTA":
            QMessageBox.information(self, "Resultado", "¡Respuesta correcta!")
        else:
            QMessageBox.information(self, "Resultado", "Respuesta incorrecta. Por favor, inténtalo de nuevo.")
               
class darInfoFrontal(QMainWindow):
        def __init__(self,ppal=None):
            super().__init__(ppal)
            loadUi("info.ui",self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setup()

        def setup(self):
            self.minimizar.clicked.connect(self.minimizarVentana)
            self.salir.clicked.connect(self.salirVentana)

        def set_coordinador(self, coordinador):
            self.coordinador = coordinador
        
        def minimizarVentana(self):
            self.showMinimized()
    
        def salirVentana(self):
            self.hide()

        def mostrar(self):
            resultado=self.coordinador.extraer_info(3)
            self.informacion.setText(str(resultado))
    
class darInfoParietal(QMainWindow):
        def __init__(self,ppal=None):
            super().__init__(ppal)
            loadUi("info.ui",self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setup()

        def setup(self):
            self.minimizar.clicked.connect(self.minimizarVentana)
            self.salir.clicked.connect(self.salirVentana)

        def set_coordinador(self, coordinador):
            self.coordinador = coordinador
        
        def minimizarVentana(self):
            self.showMinimized()
    
        def salirVentana(self):
            self.hide()

        def mostrar(self):
            resultado=self.coordinador.extraer_info(4)
            self.informacion.setText(str(resultado))

class darInfoOccipital(QMainWindow):
        def __init__(self,ppal=None):
            super().__init__(ppal)
            loadUi("info.ui",self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setup()

        def setup(self):
            self.minimizar.clicked.connect(self.minimizarVentana)
            self.salir.clicked.connect(self.salirVentana)

        def set_coordinador(self, coordinador):
            self.coordinador = coordinador
        
        def minimizarVentana(self):
            self.showMinimized()
        
        def salirVentana(self):
            self.hide()

        def mostrar(self):
            resultado=self.coordinador.extraer_info(2)
            self.informacion.setText(str(resultado))

class darInfoTemporal(QMainWindow):
        def __init__(self,ppal=None):
            super().__init__(ppal)
            loadUi("info.ui",self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setup()

        def setup(self):
            self.minimizar.clicked.connect(self.minimizarVentana)
            self.salir.clicked.connect(self.salirVentana)

        def set_coordinador(self, coordinador):
            self.coordinador = coordinador
        
        def minimizarVentana(self):
            self.showMinimized()
        
        def salirVentana(self):
            self.hide()

        def mostrar(self):
            resultado=self.coordinador.extraer_info(1)
            self.informacion.setText(str(resultado))

class darInfoCerebelo(QMainWindow):
        def __init__(self,ppal=None):
            super().__init__(ppal)
            loadUi("info.ui",self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setup()

        def setup(self):
            self.minimizar.clicked.connect(self.minimizarVentana)
            self.salir.clicked.connect(self.salirVentana)

        def set_coordinador(self, coordinador):
            self.coordinador = coordinador
        
        def minimizarVentana(self):
            self.showMinimized()
        
        def salirVentana(self):
            self.hide()

        def mostrar(self):
            resultado=self.coordinador.extraer_info(5)
            self.informacion.setText(str(resultado))

class darInfoEspinal(QMainWindow):
        def __init__(self,ppal=None):
            super().__init__(ppal)
            loadUi("info.ui",self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setup()

        def setup(self):
            self.minimizar.clicked.connect(self.minimizarVentana)
            self.salir.clicked.connect(self.salirVentana)

        def set_coordinador(self, coordinador):
            self.coordinador = coordinador
        
        def minimizarVentana(self):
            self.showMinimized()
        
        def salirVentana(self):
            self.hide()

        def mostrar(self):
            resultado=self.coordinador.extraer_info(6)
            self.informacion.setText(str(resultado))

class agregrar_E(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("agregar.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup()
    
    def setup(self):
        self.GUARDAR.clicked.connect(self.guardarEnfermedad)
        self.GUARDAR_IMAGEN.clicked.connect(self.cargarImagen)
        self.minimizar.clicked.connect(self.minimizarVentana)
        self.salir.clicked.connect(self.salirVentana)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def minimizarVentana(self):
            self.showMinimized()
        
    def salirVentana(self):
        self.hide()
    
    def guardarEnfermedad(self):
        ide=self.codigo.text()
        nombre=self.nombre.text()
        sintomas=self.sintomas.text()
        especialista=self.especialistas.text()
        tratamiento=self.tratamiento.text()
        resultado=self.coordinador.ingresarInfo(ide,nombre,sintomas,tratamiento,especialista)
        if resultado == "Error: Ya existe una enfermedad con el mismo ID.":
            QMessageBox.information(self,"" ,"Error: Ya existe una enfermedad con el mismo ID.")
        else:
            ide=self.codigo.text()
            nombre=self.nombre.text()
            sintomas=self.sintomas.text()
            especialista=self.especialistas.text()
            tratamiento=self.tratamiento.text()
            self.coordinador.ingresarInfo(ide,nombre,sintomas,tratamiento,especialista)
            QMessageBox.information(self,"" ,"¡Enfermedad ingresada a la base con éxito!")
    
    def cargarImagen(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona una imagen", "", "Images (*.png *.xpm *.jpg *.jpeg)", options=options)
        if fileName:
            pixmap = QPixmap(fileName)
            self.label_IMAGEN.setPixmap(pixmap.scaled(self.label_IMAGEN.size(), aspectRatioMode=True))
    
class buscar_E(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("buscar.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup()
    
    def setup(self):
        self.BUSCAR.clicked.connect(self.buscarEnfermedad)
        self.minimizar.clicked.connect(self.minimizarVentana)
        self.salir.clicked.connect(self.salirVentana)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def minimizarVentana(self):
            self.showMinimized()
        
    def salirVentana(self):
        self.hide()
    
    def buscarEnfermedad(self):
        nombre=self.nombre.text()
        resultado=self.coordinador.buscarEnfermedad(nombre)
        if resultado is None:
            QMessageBox.information(self,"" ,"¡No hay ningúna enfermedad que coincida!")
        else:
            self.informacion.setText(str(resultado))

class borrar_E(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("borrar.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup()
    
    def setup(self):
        self.BORRAR.clicked.connect(self.borrarEnfermedad)
        self.minimizar.clicked.connect(self.minimizarVentana)
        self.salir.clicked.connect(self.salirVentana)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def minimizarVentana(self):
            self.showMinimized()
        
    def salirVentana(self):
        self.hide()
    
    def borrarEnfermedad(self):
        codigo=self.CODIGO.text()
        resultado=self.coordinador.borrarEnfermedad(codigo)
        if resultado == "Error: No se encontró ninguna enfermedad con la ID proporcionada.":
            QMessageBox.information(self,"" ,"¡No hay ningúna enfermedad que coincida!")
        else:
            QMessageBox.information(self,"" ,"¡Enfermedad borrada con éxito de la base!")
    

        

    
    
    