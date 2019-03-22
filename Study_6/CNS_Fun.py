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
from ui_data.gui_study_6 import Ui_Dialog

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MyForm(QDialog):
    def __init__(self, mem):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.mem = mem

        self.draw_power_gp()
        self.draw_turbin_gp()

        self.blick_switch = True

        # x msec마다 업데이트
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_gp)
        timer.timeout.connect(self.update_label)
        timer.timeout.connect(self.update_alarm)
        timer.start(500)

        self.show()

    def update_alarm(self):
        # rgb(227, 227, 227) : red, rgb(255, 0, 0): gray
        if self.mem['KLAMPO21']['V'] == 1:
            self.ui.arlarm_1.setStyleSheet("background-color: rgb(227, 227, 227);")
        elif self.mem['KLAMPO21']['V'] == 0:
            self.ui.arlarm_1.setStyleSheet("background-color: rgb(255, 0, 0);")

        if self.mem['KLAMPO22']['V'] == 1:
            self.ui.arlarm_2.setStyleSheet("background-color: rgb(227, 227, 227);")
        elif self.mem['KLAMPO22']['V'] == 0:
            self.ui.arlarm_2.setStyleSheet("background-color: rgb(255, 0, 0);")

        if self.blick_switch:
            self.ui.arlarm_3.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.blick_switch = False
        else:
            self.ui.arlarm_3.setStyleSheet("background-color: rgb(227, 227, 227);")
            self.blick_switch = True

    def update_label(self):
        self.ui.power_label_1.setText('Reactor Power : {:0.2f}[%]'.format(self.mem['QPROLD']['V']*100))
        self.ui.turbine_label_1.setText('Turbine Load : {}[Mwe]'.format(self.mem['KBCDO22']['V']))
        self.ui.power_label_2.setText('{:0.2f}[%]'.format(self.mem['QPROLD']['V']*100))
        self.ui.turbine_label_2.setText('{}[Mwe]'.format(self.mem['KBCDO22']['V']))

    def update_gp(self):
        # self.ui.label.setText("{}".format(self.mem['QPROLD']['V']))
        self.p_ax.clear()
        self.t_ax.clear()
        tempx = [x for x in range(0, len(self.mem['QPROLD']['L']))]
        self.p_ax.plot(self.mem['QPROLD']['L'])
        self.p_ax.set_ylim(-0.2, 1.2)
        self.p_ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        self.p_ax.set_yticklabels([0, 25, 50, 75, 100])

        self.t_ax.plot(self.mem['KBCDO22']['L'])

        self.p_ax.grid()
        self.t_ax.grid()
        self.p_fig.tight_layout(pad=0.1)
        self.t_fig.tight_layout(pad=0.1)
        self.p_canvas.draw()
        self.t_canvas.draw()

    def draw_power_gp(self):
        self.p_fig = plt.figure()
        self.p_ax = self.p_fig.add_subplot(111)
        # self.ax1 = self.fig.add_subplot(122)
        self.p_canvas = FigureCanvasQTAgg(self.p_fig)
        self.ui.power_layout.addWidget(self.p_canvas)

    def draw_turbin_gp(self):
        self.t_fig = plt.figure()
        self.t_ax = self.t_fig.add_subplot(111)
        # self.ax1 = self.fig.add_subplot(122)
        self.t_canvas = FigureCanvasQTAgg(self.t_fig)
        self.ui.power_layout_2.addWidget(self.t_canvas)


class interface_function(multiprocessing.Process):
    def __init__(self, mem):
        multiprocessing.Process.__init__(self)
        self.mem = mem[0]

    def run(self):
        app = QApplication(sys.argv)
        w = MyForm(self.mem)
        w.exec()
        sys.exit(app.exec_())