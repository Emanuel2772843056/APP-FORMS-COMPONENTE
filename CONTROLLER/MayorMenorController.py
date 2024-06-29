from PyQt5 import QtWidgets, uic 
from SERVICE import MayorMenorService

class MayorMenorController:

    def __init__(self) -> None:
        app =QtWidgets.QApplication([])
        self.ventana = uic.loadUi("VIEW/fmmayormenor.ui")
        self.ventana.PBCALCULA2.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()
    def onclickbtncalcular(self):
        resultado = 0

        try:
            n1 = int(self. ventana.lineEdit.text())
            n2 = int(self. ventana.lineEdit_2.text())
            n3 = int(self. ventana.lineEdit_3.text())
            n4 = int(self. ventana.lineEdit_4.text())
            if self.ventana.RBMAYOR.isChecked():
                resultado= MayorMenorService.mayor(n1,n2,n3,n4)
            elif self.ventana.RBMENOR.isChecked():
                resultado = MayorMenorService.menor(n1,n2,n3,n4)
            else:
                resultado = 0
        except:
            resultado = 0
        finally:
            self.ventana.label_6.setText(str(resultado))


