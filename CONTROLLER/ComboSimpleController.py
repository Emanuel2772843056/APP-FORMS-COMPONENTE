from PyQt5 import QtWidgets, uic 

class ComboSimpleController:

    def __init__(self) -> None:
        app =QtWidgets.QApplication([])
        self.ventana = uic.loadUi("VIEW/frmlistadesplegable.ui")
        self.ventana.show()
        app.exec()