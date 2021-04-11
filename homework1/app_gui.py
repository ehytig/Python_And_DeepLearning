# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from utils import paper

class InputDialogDemo(QWidget):
    def __init__(self,parent=None):
        super(InputDialogDemo,self).__init__(parent)

        layout = QFormLayout()

        self.btn1 = QPushButton("PDF存放目录")
        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("RIS存放目录")
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("文献网页URL")
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        self.btn4 = QPushButton("Download")
        self.btn4.clicked.connect(self.download)
        layout.addRow(self.btn4)

        self.setLayout(layout)
        self.setWindowTitle('文献抓取')

    def download(self):
        pdf_directory = self.le1.text()
        if len(pdf_directory) == 0:
            pdf_directory = None
        ris_directory = self.le2.text()
        if len(ris_directory) == 0:
            ris_directory = None
        web_url = self.le3.text()
        
        paper1 = paper(web_url, pdf_directory= pdf_directory, ris_directory= ris_directory)
        paper1.download()


if __name__ == '__main__':
  app=QApplication(sys.argv)
  demo=InputDialogDemo()
  demo.show()
  sys.exit(app.exec_())

        
