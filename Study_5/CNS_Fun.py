import multiprocessing
import time


class function1(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem[0] # main mem connection

    def run(self):
        while True:
            print(self, self.mem['QPROLD'])
            time.sleep(1)


class function2(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem
        self.mem2 = mem[2]

    def run(self):
        while True:
            # print(self, self.mem[1]['Test'], '->', 1, self.mem2)
            self.mem[1]['Test'] = 1
            self.mem[2].append(1)
            time.sleep(1)


class function3(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem
        self.mem2 = mem[2]

    def run(self):
        while True:
            # print(self, self.mem[1]['Test'], '->', 2, self.mem2)
            self.mem[1]['Test'] = 2
            self.mem[2].append(2)
            time.sleep(3)

#========================================================================


class t_function1(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem[0] # main mem connection

    def run(self):
        para = ['KMSISO']
        while True:
            print(self, self.mem['KCNTOMS']['V'])
            time.sleep(1)


#========================================================================
# Interface part
#========================================================================
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from ui_data.gui_study_2 import *


class MyForm(QDialog):
    def __init__(self, mem):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.mem = mem


        self.ui.pushButton.clicked.connect(self.function_1)
        self.ui.pushButton_2.clicked.connect(self.function_2)

        # x msec마다 업데이트
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.function_2)
        timer.timeout.connect(self.function_3)
        timer.start(500)

        self.show()

    def function_1(self):
        print(self.ui.lineEdit.text())
        if self.ui.lineEdit.text() == "초기화":
            self.count = 0
            self.ui.label_2.setText("Count : {}".format(self.count))
        self.ui.label_3.setText("My name : " + self.ui.lineEdit.text())

    def function_2(self):
        self.ui.label_2.setText("{}".format(self.mem['QPROLD']['V']))

    def function_3(self):
        print('time out')

class interface_function(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem[0]

    def run(self):
        app = QApplication(sys.argv)
        w = MyForm(self.mem)
        w.exec()
        sys.exit(app.exec_())