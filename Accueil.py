import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget, QTextEdit, QLabel)
from PyQt5 import QtGui
from PyQt5 import QtCore
from fenetre_dossier import View

class View_main(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

        self.fenetre_dossier = View(self)

        self.photo = QLabel(self)
        self.photo.setPixmap(QtGui.QPixmap('logo.jpg'))
        self.photo.setAlignment(QtCore.Qt.AlignCenter)

        self.nom_plateforme = QLabel('Doctissolib')
        self.message = QLabel("Bienvenue chez nous. Ne vous inquiétez plus, on s'occupe de tout")
        self.nom_plateforme.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.b1 = QPushButton("Créer un dossier",clicked= lambda : self.creer_dossier(View_main))
        self.b2 = QPushButton("Importer un dossier")

        self.init_ui()

        self.show()

    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.photo)
        v_box.addWidget(self.nom_plateforme)
        v_box.addWidget(self.message)


        h_box = QHBoxLayout()
        v_box.addLayout(h_box)
        h_box.addWidget(self.b1)
        h_box.addWidget(self.b2)

        self.setLayout(v_box)
        self.setWindowTitle('Doctissolib')

        self.b2.clicked.connect(self.importer_dossier)

    def creer_dossier(self,View_main):

        self.hide()
        self.fenetre_dossier.show()


    def importer_dossier(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View_main()
    sys.exit(app.exec_())
