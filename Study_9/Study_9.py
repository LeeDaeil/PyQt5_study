import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_data.gui_study_9 import *
import Study_9_re_rc # resource file

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.background_setting()
        self.initial_interface()
        # self.show()

    def background_setting(self):
        self.back_color ={
            'gray': "background-color: rgb(229, 229, 229);",
            'green': "background-color: rgb(0, 170, 0);",
            'yellow': "background-color: rgb(0, 170, 0);",
            'orange': "background-color: rgb(255, 85, 0);",
            'red': "background-color: rgb(255, 0, 0);",
        }
        self.back_img = {
            'P_1_ON': "image: url(:/Sys/Pump_1_ON.png);",       # P_1~6
            'P_1_OFF': "image: url(:/Sys/Pump_1_OFF.png);",     # P_1~6
            'P_2_ON': "image: url(:/Sys/Pump_2_ON.png);",       # P_7~9
            'P_2_OFF': "image: url(:/Sys/Pump_2_OFF.png);",     # P_7~9
            'P_3_ON': "image: url(:/Sys/Pump_3_ON.png);",       # P_7~9
        }

    def initial_interface(self):
        self.ui.CSF_1_1.setStyleSheet(self.back_color['gray'])
        self.ui.CSF_1_2.setStyleSheet(self.back_color['gray'])
        self.ui.P_1.setStyleSheet(self.back_img['P_1_OFF'])

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
