# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_mainwindow import Ui_MainWindow

class Calc:
    currText:str

    oldNumber:float
    currNumber:float

    def __init__(self):
        self.currText = ""

    def AddText(self, text:str, ui:Ui_MainWindow):
        self.currText += text
        self.SetText(ui)

    def SetText(self, ui:Ui_MainWindow):
        ui.Text.setText(self.currText)

class Window(QMainWindow):
    ui:Ui_MainWindow
    calc:Calc

    def __init__(self, x = 0, y = 0, w = 640, h = 480):
        self.calc = Calc()
        super().__init__()
        self.setGeometry(x, y, w, h)
        self.setWindowTitle("Calculator")
        self.InitUI()

    def InitUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.UICheck()

    def UICheck(self):
        for i in range(0, 10):
           getattr(self.ui, "Num_" + str(i)).clicked.connect(self.OnClick)

        self.ui.Modulo.clicked.connect(self.Test)

    def Test(self):
        print("to")

    def OnClick(self):
        button = self.sender()
        self.calc.AddText(button.text(), self.ui)

def main():
    app = QApplication(sys.argv)
    win = Window()

    app.activeWindow()
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
