from PyQt5 import QtWidgets, uic 
from  SERVICE import CalculadoraService
class CalculadoraController:

    def __init__(self) -> None:
        app =QtWidgets.QApplication([])
        self.ventana = uic.loadUi("VIEW/fmcalculador.ui")
        self.ventana.PBCALCULA.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()
    def onclickbtncalcular(self):
        resultado = 0
        operacion = ""

        try:
            num1 = int(self.ventana.txtlineEdit.text())
            num2 = int(self.ventana.txtlineEdit_2.text())
            if self.ventana.RBSUMA.ischecked():
                resultado = CalculadoraService.suma(num1, num2)
                operacion ="suma"
            elif self.ventana.RBRESTA.ischecked():
                resultado = CalculadoraService.resta(num1, num2)
                operacion ="resta"
            elif self.ventana.RBMULTIPLICACION.ischecked():
                resultado = CalculadoraService.multiplica(num1, num2)
                operacion ="multiplica"
            elif self.ventana.RBDIVIDE.ischecked():
                resultado = CalculadoraService.divide(num1, num2)
                operacion ="divide"
            else:
                resultado = 0
                operacion = "Elegir operacion"
        except:
            operacion ="Ingrese valor numericos"
        finally:
            self.ventana.label_4.setText(operacion+"="+ str(resultado))

        
        