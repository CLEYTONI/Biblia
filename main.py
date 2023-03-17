from Biblia import Ui_Form
from  PyQt5.QtWidgets import QApplication, QWidget
import sys
from read_json import read_json
import requests
from testes import teste, dicionario, result


class Main(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Main, self).__init__()
        self.setupUi(self)

        self.pesquisa_button.clicked.connect(self.find_versiculo)

    
    def find_versiculo(self):
        livro = read_json(self.livro_edit.text())
        capitulo = self.capitulo_edit.text()
        versiculos = self.request_biblia(livro, capitulo)
        
        variavel = ''
        for x in versiculos:
            for y, z in x.items():
                variavel += str(z)+'\n'
                
        self.versiculo_label.setText(variavel)

    def request_biblia(self, livro, capitulo):
        print(livro)
        link = f'https://www.abibliadigital.com.br/api/verses/nvi/{livro}/{capitulo}'
        api = requests.get(link).json()
        versiculos = api['verses']
        return versiculos



if __name__ == '__main__':
    execute = QApplication(sys.argv)
    projeto = Main()
    projeto.show()
    execute.exec_()