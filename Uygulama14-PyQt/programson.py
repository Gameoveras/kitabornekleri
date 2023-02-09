import sys
import sqlite3
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


baglanti = sqlite3.connect("yeni.db")

app = QApplication(sys.argv)

class Kayit(QWidget):
    def __init__(self):
        super().__init__()
        self.arayüz()
        self.komutlar()
        self.window1 = Profil()
    def arayüz(self):
        layout = QVBoxLayout()

        self.resize(350, 350)
        self.move(650, 150)
        self.setWindowTitle('Kaydol Bölümü')

        self.setLayout(layout)
    def komutlar(self):
        self.input1 = QLineEdit("Ad-Soyad Gir", self)
        self.input1.setGeometry(20, 70, 200, 25)
        self.input2 = QLineEdit("E-posta Gir", self)
        self.input2.setGeometry(20, 100, 200, 25)
        self.input3 = QLineEdit("Parola Gir", self)
        self.input3.setGeometry(20, 130, 200, 25)
        button1 = QPushButton("Kaydol", self)
        button1.setGeometry(20, 170, 150, 25)
        button1.clicked.connect(
           lambda checked: self.toggle_window(self.window1)
        )
   
    def kaydet(self):
        a = self.input1.text()
        b = self.input2.text()
        c = self.input3.text()

        baglanti.execute("INSERT INTO kullanici (adsoyad,eposta,sifre) Values (?,?,?)" , (a, b, c))
        baglanti.commit()
        lambda checked: self.toggle_window(self.window1) 
            
  
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()
    
            
            
class Profil(QWidget):
    def __init__(self):
        super().__init__()
        self.arayüz()
    def arayüz(self):
        layout = QVBoxLayout()
        self.window1 = Saticilar()
        self.window2 = Urunekle()
        self.resize(500, 500)
        self.move(750, 150)
        self.setWindowTitle('Profilim Bölümü')

        self.setLayout(layout)
        
        button1 = QPushButton("Satıcılar", self)
        button1.setGeometry(20, 130, 250, 25)
        button2 = QPushButton("Ürün ekle", self)
        button2.setGeometry(20, 160, 250, 25)
       
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        layout.addWidget(button1)
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        layout.addWidget(button2)

       
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()
        
        
        
class Saticilar(QListWidget):
     def __init__(self):
        super().__init__()
        self.arayüz()
        
     def arayüz(self):
        

        self.resize(500, 500)
        self.move(750, 150)
        self.setWindowTitle('Satıcılar Bölümü')
        self.setStyleSheet('font-size: 35px')
        
        
        kisiler = baglanti.execute('SELECT adsoyad FROM kullanici').fetchall()
        for kisi in kisiler:
            self.addItem(str(kisi))
        

        
          

class Urunekle(QWidget):
    def __init__(self):
        super().__init__()
        self.arayüz()
        self.komutlar()
    def arayüz(self):
        layout = QVBoxLayout()

        self.resize(500, 500)
        self.move(750, 150)
        self.setWindowTitle('Ürün ekleme Bölümü')

        self.setLayout(layout)
    def komutlar(self):
        self.input1 = QLineEdit("Ürün adını Gir", self)
        self.input1.setGeometry(20, 70, 200, 25)
        self.input2 = QLineEdit("Ürün Açıklaması Gir", self)
        self.input2.setGeometry(20, 100, 200, 25)
        self.input3 = QLineEdit("Ürün Fiyatı Gir", self)
        self.input3.setGeometry(20, 130, 200, 25)
        button1 = QPushButton("Kaydet", self)
        button1.setGeometry(20, 160, 150, 25)
    
        button1.clicked.connect(self.kaydet)
    def kaydet(self):
        try:
            a = self.input1.text()
            b = self.input2.text()
            c = self.input3.text()
            baglanti.execute("INSERT INTO urun (adsoyad,eposta,sifre) Values (?,?,?)" , (a, b, c))
            baglanti.commit()
        except:
            print("hata")
        finally:
            pass
            
  
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()
       
          
    
class Kayıtpe(QWidget):
    def __init__(self):
        super().__init__()
        self.arayüz()
        self.komutlar()
        self.window1 = Profil()
        self.window2 = Kayit()

    def arayüz(self):
        layout = QVBoxLayout()

        self.resize(350, 350)
        self.move(650, 150)
        self.setWindowTitle('Giriş Yap Bölümü')

        self.setLayout(layout)

    def komutlar(self):
        self.input1 = QLineEdit("Eposta Gir", self)
        self.input1.setGeometry(20, 70, 200, 25)
        self.input2 = QLineEdit("Parola Gir", self)
        self.input2.setGeometry(20, 100, 200, 25)
        button1 = QPushButton("Giriş Yap", self)
        button1.setGeometry(20, 130, 150, 25)
        button3 = QPushButton("Kaydol", self)
        button3.setGeometry(20, 160, 150, 25)
        
       

        button1.clicked.connect(self.kantrol)
        button3.clicked.connect(
            lambda checked: self.toggle_window(self.window2)  
        )
       
        
        
        
    
    def kantrol(self):
        kisiler = baglanti.execute('SELECT * FROM kullanici').fetchall()
        for kisi in kisiler:
                if kisi[2] == self.input1.text():
                    if kisi[3] == self.input2.text():
                        lambda checked: self.toggle_window(self.window1)  
        
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()
    



class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.arayüz()
        self.komutlar()
        self.window1 = Kayıtpe()
        self.window2 = Kayit()

    def arayüz(self):
        self.resize(350, 350)
        self.move(650, 150)
        self.setWindowTitle('Giriş Bölümü')

    def komutlar(self):
        l = QVBoxLayout()
        button1 = QPushButton("Giriş Yap", self)
        button1.setGeometry(20, 50, 250, 25)

        button3 = QPushButton("Kaydol", self)
        button3.setGeometry(20, 70, 250, 25)

        self.label = QLabel("E-ticaret programına hoşgeldiniz", self)
        self.label.setGeometry(10, 0, 200, 75)

        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)
        button3.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button3)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

   

pencere = Pencere()
pencere.show()
sys.exit(app.exec_())
