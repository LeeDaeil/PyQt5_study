import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_data.gui_study_9 import *
import Study_9.Study_9_re_rc

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
