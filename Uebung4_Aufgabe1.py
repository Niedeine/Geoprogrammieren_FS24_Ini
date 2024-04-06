import sys
import os
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        #Menu erstellen:
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)

        self.quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" zuweisen, nur für MacOS relevant


        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)

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



        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag", self.dobLineEdit)
        layout.addRow("Adresse",self.adresseLineEdit)
        layout.addRow("Postleitzahl",self.plzLineEdit)
        layout.addRow("Ort",self.ortLineEdit)
        layout.addRow("Land",self.countries)
        layout.addRow(self.button1)
  
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


    def speichern(self):
        vorname = self.vornameLineEdit.text()
        name=self.nameLineEdit.text()
        geburtstag=self.dobLineEdit.text()
        adresse=self.adresseLineEdit.text()
        postleitzahl=self.plzLineEdit.text()
        ort=self.ortLineEdit.text()
        Land=self.countries.currentText()

        datei=open("output.txt", "a")
        datei.write(f"{vorname},{name},{geburtstag},{adresse},{postleitzahl},{ort},{Land}\n")
        datei.close()
        
        QMessageBox.about(self,"Info","Ihr Datensatz wurde")

    def schliesen(self):
        self.close()




def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()