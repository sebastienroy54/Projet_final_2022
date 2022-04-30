import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget, QTextEdit, QLabel, QRadioButton)

class View_historique(QWidget):
    def __init__(self,viewA,nom,prenom,age,sexe):
        super().__init__()
        self.viewA = viewA
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe

        self.nom_text = QLabel('Nom')
        self.prenom_text = QLabel('Prenom')
        self.age_text = QLabel('Age')

        self.nom_edit = QLineEdit()
        self.prenom_edit = QLineEdit()
        self.age_edit = QLineEdit()

        self.histTitle = QLabel('Historique du patient')

        self.historique = QTextEdit()

        self.fermer = QPushButton('Fermer')

        self.init_ui()

    def init_ui(self):
        HD_box = QVBoxLayout()
        HG_box = QVBoxLayout()

        HG_box.addWidget(self.nom_text)
        HG_box.addWidget(self.prenom_text)
        HG_box.addWidget(self.age_text)

        HD_box.addWidget(self.nom_edit)
        HD_box.addWidget(self.prenom_edit)
        HD_box.addWidget(self.age_edit)

        HH_box = QHBoxLayout()
        HH_box.addLayout(HG_box)
        HH_box.addLayout(HD_box)

        h_box = QVBoxLayout()
        h_box.addWidget(self.histTitle)
        h_box.addWidget(self.historique)
        h_box.addWidget(self.fermer)

        H_box = QVBoxLayout()
        H_box.addLayout(HH_box)
        H_box.addLayout(h_box)

        self.setLayout(H_box)
        self.setWindowTitle('fenetre_historique')
        self.fermer.clicked.connect(self.btn_fermer)

        self.historique.setDisabled(True)
        self.nom_edit.setDisabled(True)
        self.prenom_edit.setDisabled(True)
        self.age_edit.setDisabled(True)

        self.nom_edit.setText(self.nom)
        self.prenom_edit.setText(self.prenom)
        self.age_edit.setText(self.age)

        f = open(self.nom + " " + self.prenom + ".txt", "r")
        self.info = f.read()
        tampon = self.info.split(self.sexe)
        tampon2 = tampon[1]
        tampon3 = tampon2.split("\n",1)
        self.sympt = tampon3[1]
        f.close()
        self.historique.setText(self.sympt)

    def btn_fermer(self):
        self.hide()
        self.viewA.show()
