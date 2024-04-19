import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QLabel
from PyQt5.QtWidgets import QAction,QMainWindow,QApplication,qApp



class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.sayi_liste = list()

        self.yazi_alani = QLabel(self)
        
        self.grid = QGridLayout()


        self.num1 = QPushButton("1")
        self.num2 = QPushButton("2")
        self.num3 = QPushButton("3")
        self.num4 = QPushButton("4")
        self.num5 = QPushButton("5")
        self.num6 = QPushButton("6")
        self.num7 = QPushButton("7")
        self.num8 = QPushButton("8")
        self.num9 = QPushButton("9")
        self.num0 = QPushButton("0")
        self.top = QPushButton("+")
        self.cik = QPushButton("-")
        self.cap = QPushButton("x")
        self.bol = QPushButton(":")
        self.hesapla = QPushButton("=")
        self.temizle = QPushButton("Clear")
        
        self.grid.addWidget(self.yazi_alani,0,0)
        self.grid.addWidget(self.num1,2,0)
        self.grid.addWidget(self.num2,2,1)
        self.grid.addWidget(self.num3,2,2)
        self.grid.addWidget(self.top,2,3)
        self.grid.addWidget(self.num4,3,0)
        self.grid.addWidget(self.num5,3,1)
        self.grid.addWidget(self.num6,3,2)
        self.grid.addWidget(self.cik,3,3)
        self.grid.addWidget(self.num7,4,0)
        self.grid.addWidget(self.num8,4,1)
        self.grid.addWidget(self.num9,4,2)
        self.grid.addWidget(self.cap,4,3)
        self.grid.addWidget(self.temizle,5,0)
        self.grid.addWidget(self.num0,5,1)
        self.grid.addWidget(self.hesapla,5,2)
        self.grid.addWidget(self.bol,5,3)

        self.setLayout(self.grid)       

        self.num1.clicked.connect(self.rakam_1)
        self.num2.clicked.connect(self.rakam_2)
        self.num3.clicked.connect(self.rakam_3)
        self.num4.clicked.connect(self.rakam_4)
        self.num5.clicked.connect(self.rakam_5)
        self.num6.clicked.connect(self.rakam_6)
        self.num7.clicked.connect(self.rakam_7)
        self.num8.clicked.connect(self.rakam_8)
        self.num9.clicked.connect(self.rakam_9)
        self.num0.clicked.connect(self.rakam_0)
        self.top.clicked.connect(self.toplama)
        self.cik.clicked.connect(self.cikarma)
        self.cap.clicked.connect(self.carpma)
        self.bol.clicked.connect(self.bolme)
        self.temizle.clicked.connect(self.temizleme)
        self.hesapla.clicked.connect(self.hesaplama)

    def rakam_1(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 1 ")

    def rakam_2(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 2 ")

    def rakam_3(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 3 ")

    def rakam_4(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 4 ")
    def rakam_5(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 5 ")

    def rakam_6(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 6 ")

    def rakam_7(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 7 ")

    def rakam_8(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 8 ")

    def rakam_9(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 9 ")
    
    def rakam_0(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " 0 ")


    def toplama(self):
        
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " + ")

    def cikarma(self):
         
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " - ")

    def carpma(self):
        
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " * ")  

    def bolme(self):
        text = self.yazi_alani.text()
        self.yazi_alani.setText(text + " / ")

    def temizleme(self):
        self.yazi_alani.clear()

    def hesaplama(self):
        equation = self.yazi_alani.text()
        try:
            ans = eval(equation)
            self.yazi_alani.setText(str(ans))
        except:
            self.yazi_alani.setText("Yanlış Değer")    

class Menu(QMainWindow):
    def __init__(self):

        super().__init__()

        self.pencere = Pencere()

        self.setCentralWidget(self.pencere)

        self.menu_olustur()

    def menu_olustur(self):
        
        menu_bar = self.menuBar()

        self.menu = menu_bar.addMenu("Menu")

        clear = QAction("Clear",self)
        clear.setShortcut("Ctrl+D")
        cikis = QAction("Quit",self)
        cikis.setShortcut("Ctrl+Q")
        hesapla = QAction("Equal",self)

        self.menu.addAction(clear)
        self.menu.addAction(cikis)
        self.menu.addAction(hesapla)

        self.setWindowTitle("Hesap Makinesi")

        self.menu.triggered.connect(self.response)

    def response(self,response):

        if response.text() == "Clear":
            self.pencere.temizleme()
        
        if response.text() == "Quit":
            qApp.quit()

        if response.text() == "Equal":
            self.pencere.hesaplama()

app = QApplication(sys.argv)

menu = Menu()

menu.show()

sys.exit(app.exec_())