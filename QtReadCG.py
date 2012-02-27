# -*- coding: latin1 -*-
# python  QtReadCG.py

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Brazilian Verbs")
        self.resize(500,100)

        MyDictionary = self.getdata()
        MyVerbs = sorted(self.MyVerbs.keys())
        currentverbindex = 0
        currentverb = MyVerbs[currentverbindex]
        MyParts  = self.MyVerbs[currentverb]
        MyDictionaryLabel = QLabel(MyDictionary)

        self.InfinitiveComboBox = QComboBox()
        self.InfinitiveComboBox.addItems(MyVerbs)

        self.PartsComboBox = QComboBox()
        self.PartsComboBox.addItems(MyParts)

        self.MyLineEdit = QLineEdit()
        self.MySpinBox =  QSpinBox()
        self.MyDial =  QDial()
        self.MyDial.setNotchesVisible(True)

        grid = QGridLayout()
        grid.addWidget(MyDictionaryLabel, 0, 0)
        grid.addWidget(self.MyDial, 1, 0)
        grid.addWidget(self.MyLineEdit, 2, 0)
        grid.addWidget(self.MySpinBox, 2, 1)
        grid.addWidget(self.InfinitiveComboBox, 3, 0)
        grid.addWidget(self.PartsComboBox, 3, 1)

        self.setLayout(grid)


        self.connect(self.InfinitiveComboBox,
                SIGNAL("currentIndexChanged(int)"), self.updateUi)

        self.connect(self.PartsComboBox,
                SIGNAL("currentIndexChanged(int)"), self.updateUi)



    def updateUi(self):
        print 'self.updateUi called...'
#        inf = unicode(self.InfinitiveComboBox.currentText())
#        parts = unicode(self.PartsComboBox.currentText())


    def getdata(self): 
        #self.rates = {'Euro':10, 'Pound':11}  #######
        BigDict = {}   
        f = open('cg-out.txt','r')
        lastlineofverb = False
        partlist = []

        for line in f.readlines():
            tenseline = line.split(':')
            if tenseline[0] == 'IS':
                partlist = []
            elif tenseline[0] == 'FN':
                infinitive = tenseline[1]
            elif tenseline[0] == 'EI':
                lastlineofverb = True

            tenseline = tenseline[1:]

            for word in tenseline:
               word = word.rstrip()
               # DECODE UTF-8 TO UNICODE FOR QT !!
               word = word.decode('utf-8')
               ###################################
               if word not in partlist:
                   partlist.append(word)

            if lastlineofverb:
                BigDict [infinitive] = partlist
                lastlineofverb = False

        f.close()
        self.MyVerbs = BigDict

    def printdata(self): 
        print '\n'
        print key,
        print 'Unique words: ' + str(len(BigDict[key])) 
        print '------------------------------'
        for word in BigDict[key]:
            print word,

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()










