import sys
from PyQt5.QtWidgets import QWidget, QApplication,QLabel,QLineEdit,QPushButton
from PyQt5.QtCore import pyqtSlot


app = QApplication(sys.argv)

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.arayüz()
        self.komutlar()
        
        
    def arayüz(self):
        self.resize(750, 750)
        self.move(710, 150)
        self.setWindowTitle('Yeni Pencere')
    
    def komutlar(self):
        self.input1 = QLineEdit("1.Sayıyı gir", self)
        self.input1.setGeometry(20, 70, 200, 25)
        self.input2 = QLineEdit("2.Sayıyı Gir", self)
        self.input2.setGeometry(20, 100, 200, 25)
        button1 = QPushButton("+", self)
        button1.setGeometry(20, 130, 50, 25)
        button2 = QPushButton("-", self)
        button2.setGeometry(70, 150, 50, 25)
        button3 = QPushButton("*", self)
        button3.setGeometry(20, 150, 50, 25)
        button4 = QPushButton("/", self)
        button4.setGeometry(70, 130, 50, 25)
        self.label = QLabel("Hesap Makinesine hoşgeldiniz",self)
        self.label.setGeometry(10, 0, 200, 75)
        self.label2 = QLabel("Cevap: ",self)
        self.label2.setGeometry(10, 170, 200, 75)
        
        button1.clicked.connect(self.topla)
        button2.clicked.connect(self.cikar)
        button3.clicked.connect(self.carp)
        button4.clicked.connect(self.bol)
        
    
    @pyqtSlot()
    def topla(self):
            adad = int(self.input1.text()) + int(self.input2.text())
            self.label2.setText(f"Cevap: {adad}")
            return self.label2
    def cikar(self):
            adad = int(self.input1.text()) - int(self.input2.text())
            self.label2.setText(f"Cevap: {adad}")
            return self.label2
    def carp(self):
            adad = int(self.input1.text()) * int(self.input2.text())
            self.label2.setText(f"Cevap: {adad}")
            return self.label2
    def bol(self):
            adad = int(self.input1.text()) / int(self.input2.text())
            self.label2.setText(f"Cevap: {adad}")
            return self.label2


pencere = Pencere()
pencere.show()
sys.exit(app.exec_())