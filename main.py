import csv
import sys

import clipboard
import pyperclip

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)
        self.pushButton.clicked.connect(self.openBtnClick)

    def openBtnClick(self):
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'csv (*.csv)')[0]
        readed = dict()
        res = ''
        with open(fname, 'r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
            readed = reader

        for item in readed:
            note = item['Notes']

            if 'Marker' in note:
                continue

            record_in = item['Record In'].split(':')

            record_in = record_in[1] + ':' + record_in[2]
            res += record_in + ' ' + item['Notes'] + '\n'

            clipboard.copy(res[:-1])



app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())