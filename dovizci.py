import sys
import os
from bs4 import BeautifulSoup
import requests
import time




from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbYenile = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.doviz_cek())
        self.pbYenile.setGeometry(QtCore.QRect(620, 10, 191, 41))
        self.pbYenile.setObjectName("pbYenile")
        self.pbTemzile = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.textBrowser.clear())
        self.pbTemzile.setGeometry(QtCore.QRect(620, 70, 191, 41))
        self.pbTemzile.setObjectName("pbTemzile")
        self.pbCikis = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : QtWidgets.qApp.quit())
        self.pbCikis.setGeometry(QtCore.QRect(620, 130, 191, 41))
        self.pbCikis.setObjectName("pbCikis")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 601, 561))
        self.textBrowser.setFontUnderline(True)
        self.textBrowser.setFontPointSize(15.0)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYenile = QtWidgets.QAction(MainWindow,triggered = lambda : self.doviz_cek())
        self.actionYenile.setObjectName("actionYenile")
        self.actionTemizle = QtWidgets.QAction(MainWindow,triggered = lambda : self.textBrowser.clear())
        self.actionTemizle.setObjectName("actionTemizle")
        self.actionCikis = QtWidgets.QAction(MainWindow,triggered = lambda : QtWidgets.qApp.quit())
        self.actionCikis.setObjectName("actionCikis")
        self.menuDosya.addAction(self.actionYenile)
        self.menuDosya.addAction(self.actionTemizle)
        self.menuDosya.addAction(self.actionCikis)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.doviz_cek)
        self.timer.start(1000)





        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dövizci"))
        self.pbYenile.setText(_translate("MainWindow", "Yenile"))
        self.pbTemzile.setText(_translate("MainWindow", "Temizle"))
        self.pbCikis.setText(_translate("MainWindow", "Çıkış"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.actionYenile.setText(_translate("MainWindow", "Yenile"))
        self.actionTemizle.setText(_translate("MainWindow", "Temizle"))
        self.actionCikis.setText(_translate("MainWindow", "Çıkış"))

    def doviz_cek(self):
        self.textBrowser.clear()
        url = "https://www.doviz.com/"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi, "html.parser")

        basliklar = soup.find_all("span", {"class": "name"})
        endeksler = soup.find_all("span", {"class": "value"})

        for i,j in zip(basliklar,endeksler):
            self.textBrowser.append(i.text + ": "+j.text)
    
    


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
