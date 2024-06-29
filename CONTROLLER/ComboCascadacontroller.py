from PyQt5 import QtWidgets, uic 

class ComboCascadaController:

    def __init__(self) -> None:
        app =QtWidgets.QApplication([])
        self.ventana = uic.loadUi("VIEW/fmcombocascada.ui")
        self.ventana.show()
        app.exec()