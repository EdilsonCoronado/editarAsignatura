import unittest
from src.modelo.asignatura import Asignatura
from src.logica.editAsignatura import editAsignatura
from src.modelo.declarative_base import Session

class AsignaturaTestCase ( unittest.TestCase ) :
    def setUp ( self ) :
        # Crea una gestionAsignatura para hacer las pruebas
        self.gestionAsignatura = editAsignatura ()

        # Abre la sesión
        self.session = Session ( )

        # crear asignatura
        self.asignatura1 = Asignatura ( nombreAsignatura = "Construccion de Software", nombreDocente = "Daniel Gamarra")
        self.session.add ( self.asignatura1 )
        self.session.commit ()


    def tearDown ( self ) :
        self.session = Session ( )
        asignaturas = self.session.query ( Asignatura ).all ( )
        for asignatura in asignaturas :
            self.session.delete ( asignatura )
        self.session.commit ( )
        self.session.close ( )


    def test_editar_asignatura ( self ) :
        resultado = self.gestionAsignatura.editar_asignatura (nombreAsignatura ="Estructura de datos", nombreDocente ="Daniel Gamarra")
        self.assertEqual ( resultado , True )

    def test_editar_asignatura_mismos_datos(self):
        resultado = self.gestionAsignatura.editar_asignatura (nombreAsignatura = "Construccion de Software", nombreDocente = "Daniel Gamarra" )
        self.assertEqual ( resultado , False )

    def test_editar_asignatura_datos_vacios ( self ) :
        resultado = self.gestionAsignatura.editar_asignatura (nombreAsignatura ="", nombreDocente ="")
        self.assertEqual ( resultado , False )

    def test_verificar_almacenamiento_editar_asignatura(self):
        resultado = self.gestionAsignatura.editar_asignatura(nombreAsignatura="Pruebas de software", nombreDocente="Paola Torres")

        self.session = Session()
        asignatura = self.session.query(Asignatura).filter(Asignatura.nombreAsignatura == "Pruebas de software").first()

        self.assertEqual(resultado, True)
        self.assertEqual(asignatura.nombreAsignatura, "Pruebas de software")
