"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários
programas para criações de aplicações GUI (interface Gráfica).
Também inclui diversas funcionalidades, como: acesso a base de dados,
threads, comunicação de rede, etc...
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 40px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('alguma coisa')

if __name__=="__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
