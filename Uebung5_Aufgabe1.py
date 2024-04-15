import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import urllib.parse

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        #Menu erstellen:
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        self.load = QAction ("Load",self)
        self.card = QAction("Show on GoogleMaps", self)

        self.quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant


        filemenu.addAction(self.save)
        filemenu.addAction(self.load)
        filemenu.addAction(self.quit)
        viewmenu.addAction(self.card)

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.dobLineEdit= QDateEdit()
        self.adresseLineEdit= QLineEdit()
        self.plzLineEdit=QLineEdit()
        self.ortLineEdit=QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button1 = QPushButton("Save")
        self.button2 = QPushButton("Load")
        self.button3 = QPushButton("Show on GoogleMaps")



        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag", self.dobLineEdit)
        layout.addRow("Adresse",self.adresseLineEdit)
        layout.addRow("Postleitzahl",self.plzLineEdit)
        layout.addRow("Ort",self.ortLineEdit)
        layout.addRow("Land",self.countries)
        layout.addRow(self.button3)
        layout.addRow(self.button1)
        layout.addRow(self.button2)
  
        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

        #aktionen zuordnen:
        self.button1.clicked.connect(self.speichern)
        self.save.triggered.connect(self.speichern)
        self.quit.triggered.connect(self.schliesen)
        self.button2.clicked.connect(self.laden)
        self.button3.clicked.connect(self.karte)
        self.card.triggered.connect(self.karte)
        self.load.triggered.connect(self.laden)


    def speichern(self):

        filename, typ = QFileDialog.getSaveFileName(self, "Datei speichern",
                                                    "",
                                                    "Alle (*.*)")
        
    
        vorname = self.vornameLineEdit.text()
        name=self.nameLineEdit.text()
        geburtstag=self.dobLineEdit.text()
        adresse=self.adresseLineEdit.text()
        postleitzahl=self.plzLineEdit.text()
        ort=self.ortLineEdit.text()
        Land=self.countries.currentText()

        datei=open(filename, "w")
        datei.write(f"{vorname},{name},{geburtstag},{adresse},{postleitzahl},{ort},{Land}")
        datei.close()
        
        QMessageBox.about(self,"Info","Ihr Datensatz wurde gespeichert")


    def laden(self):
        filename, typ = QFileDialog.getOpenFileName(self, 
                                                    "Datei öffnen", 
                                                    "", 
                                                    "Alle (*.*);;Python (*.py);;Text (*.txt)")
        if filename != "":        
            datei = open(filename, encoding="utf-8")
            inhalt = datei.read()
            liste=inhalt.split(",")

            self.vornameLineEdit.setText(liste[0])
            self.nameLineEdit.setText(liste[1])

            d=liste[2].split("/")
            datum=QDate(int(d[2]),int(d[1]),int(d[0]))
            self.dobLineEdit.setDate(datum)

            self.adresseLineEdit.setText(liste[3])
            self.plzLineEdit.setText(liste[4])
            self.ortLineEdit.setText(liste[5])
            self.countries.setCurrentText(liste[6])
            
            datei.close()
        else:
            QMessageBox.warning(self, "Abbruch", "Der Filedialog wurde abgebrochen, es wird nichts geöffnet!")


    def schliesen(self):
        self.close()


    def karte(self):
        query = f"{self.adresseLineEdit.text()}+{self.plzLineEdit.text()}+{self.ortLineEdit.text()}"
        a = urllib.parse.quote(query)
        link=f"https://www.google.ch/maps/place/{a}"
        print (link)
        QDesktopServices.openUrl(QUrl(link))





def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()