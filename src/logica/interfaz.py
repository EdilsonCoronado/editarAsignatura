import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from tkinter import messagebox
from src.modelo.asignatura import Asignatura
from src.logica.editAsignatura import editAsignatura
from src.modelo.declarative_base import engine, Base, session


class Interfaz(QMainWindow):

    def __init__(self):
        Base.metadata.create_all(engine)
        asign = session.query(Asignatura).filter(Asignatura.idAsignatura == 1).first()
        QMainWindow.__init__(self)
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\..\view\interfaz.ui"
        uic.loadUi(ruta, self)
        asignatura = self.output_1.text()
        docente = self.output_2.text()
        """asignatura = asign.nombreAsignatura
        docente = asign.nombreDocente"""

        self.btnAceptar.clicked.connect(self.editando)
        self.btnCancelar.clicked.connect(self.exit_app)


    def editando(self):
        asignatura = self.input_1.text()
        docente = self.input_2.text()

        if(editAsignatura.editar_asignatura(nombreAsignatura=asignatura, nombreDocente=docente)) == False:
            mensaje = messagebox.showinfo("Error", "No es posible hacer el cambio")
        else:
            mensaje = messagebox.showinfo("Guardado", "Cambio realizado con exito")
            quit(0)

    def exit_app(self):
        quit(0)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ventana=Interfaz()
    ventana.show()
    app.exec()
