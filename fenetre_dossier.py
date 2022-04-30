import sys
import os
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget, QTextEdit, QLabel, QRadioButton)
from fenetre_historique import View_historique

class View(QWidget):
    def __init__(self,viewA):
        super().__init__()
        self.viewA = viewA

        self.nom = QLabel('Nom')
        self.prenom = QLabel('Prénom')
        self.age = QLabel('Age')
        self.sexe = QLabel('Sexe')

        self.nom_edit = QLineEdit()
        self.prenom_edit = QLineEdit()
        self.age_edit = QLineEdit()

        self.m = QRadioButton("Homme")
        self.f = QRadioButton("Femme")

        self.symptome_edit = QTextEdit()
        self.medicament = QTextEdit()

        self.historique = QPushButton('Historique')
        self.enregistrer = QPushButton('Enregistrer')
        self.fermer = QPushButton('Fermer')

        self.init_ui()

    def init_ui(self):
        HD_box = QVBoxLayout()
        HG_box = QVBoxLayout()

        HG_box.addWidget(self.nom)
        HG_box.addWidget(self.prenom)
        HG_box.addWidget(self.age)
        HG_box.addWidget(self.sexe)

        HD_Radio_box=QHBoxLayout()

        HD_Radio_box.addWidget(self.m)
        HD_Radio_box.addWidget(self.f)

        HD_box.addWidget(self.nom_edit)
        HD_box.addWidget(self.prenom_edit)
        HD_box.addWidget(self.age_edit)
        HD_box.addLayout(HD_Radio_box)

        HDD_box = QVBoxLayout()
        HDD_box.addWidget(self.historique)

        H_box=QHBoxLayout()
        H_box.addLayout(HG_box)
        H_box.addLayout(HD_box)
        H_box.addLayout(HDD_box)

        BG_box = QVBoxLayout()
        BG_box.addWidget(self.symptome_edit)
        BG_box.addWidget(self.enregistrer)

        BD_box = QVBoxLayout()
        BD_box.addWidget(self.medicament)
        BD_box.addWidget(self.fermer)

        B_box = QHBoxLayout()
        B_box.addLayout(BG_box)
        B_box.addLayout(BD_box)

        G_box = QVBoxLayout()
        G_box.addLayout(H_box)
        G_box.addLayout(B_box)

        self.setLayout(G_box)
        self.setWindowTitle('fenetre_dossier')
        self.medicament.setDisabled(True)
        self.fermer.clicked.connect(self.btn_fermer)
        self.historique.clicked.connect(lambda: self.btn_historical(self.m.isChecked()))
        self.enregistrer.clicked.connect(lambda: self.btn_register(self.m.isChecked()))

        self.symptome_edit.textChanged.connect(self.medoc)

    def btn_register(self,chk):
        nom = self.nom_edit.text()
        prenom = self.prenom_edit.text()
        age = self.age_edit.text()
        symptome = self.symptome_edit.toPlainText()
        if chk:
            sexe = "Homme"
        else:
            sexe = "Femme"

        if os.path.isfile(nom + " " + prenom + ".txt") == True:
            f = open(nom + " " + prenom + ".txt", "a")
            f.write("\n" + symptome)
            f.close()
        else:
            f = open(nom + " " + prenom + ".txt", "a")
            f.write(nom + "\n" + prenom + "\n" + age + "\n" + sexe + "\n" + symptome)
            f.close()


    def btn_historical(self,chk):
        self.hide()
        nom = self.nom_edit.text()
        prenom = self.prenom_edit.text()
        age = self.age_edit.text()
        if chk:
            sexe = "Homme"
        else:
            sexe = "Femme"
        self.fenetre_historique = View_historique(self,nom,prenom,age,sexe)
        self.fenetre_historique.show()

    def btn_fermer(self):
        self.hide()
        self.viewA.show()

    def medoc(self):
        medoc = ""

        symptome = self.symptome_edit.toPlainText()
        liste = symptome.split("\n")
        Dico_medicament = {"douleur":["dolipranne","dafalgan","efferalgan"], "fievre":["dolipranne","dafalgan","efferalgan"], "cardiovasculaire":["kardegic"], "douleur a l'estomac":["spasfon"], "brulure d'estomac":["gaviscon"], "irritation cutanée":["dexeril"], "ballonement abdominal":["meteospasmyl"], "egratinure":["biseptine"], "plaie":["bispetine"], "coupure":["biseptine"], "infection de la bouche":["eludril"]}
        for k in Dico_medicament.keys():
            for i in range (len(liste)):
                if liste[i]==k:
                    med = Dico_medicament[k]
                    for i in range (len(med)):
                        medoc += med[i] + "\n"

        test = medoc.split("\n")
        newtest=[]
        tampon=""
        for i in test:
             if i not in newtest:
                 newtest.append(i)
        for i in range (len(newtest)):
            tampon+= newtest[i] + "\n"
        if medoc=="":
            pass
        else:
            self.medicament.setText(tampon)

