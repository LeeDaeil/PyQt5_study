import sys
import pickle
from PyQt5.QtWidgets import QDialog, QApplication
from ui_data.gui_study_7 import Ui_Dialog

# DB = {'gori':{}, 'new_gori':{}, 'han':{}}

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cal.clicked.connect(self.cal_function)
        self.ui.lineEdit.returnPressed.connect(self.enter_function)

        with open('DB.bin', 'rb') as f:
            self.DB = pickle.load(f)

        self.show()

    def enter_function(self):
        self.ui.out_list.clear()
        if self.ui.gori.isChecked() == True:
            print(len(self.DB['gori']))
            for _ in self.DB['gori']:
                if self.DB['gori'][_].find(self.ui.lineEdit.text()) != -1:
                    self.ui.out_list.append(_)
        if self.ui.han.isChecked() == True:
            print(len(self.DB['han']))
            for _ in self.DB['han']:
                if self.DB['han'][_].find(self.ui.lineEdit.text()) != -1:
                    self.ui.out_list.append(_)
        if self.ui.new_gori.isChecked() == True:
            print(len(self.DB['new_gori']))
            for _ in self.DB['new_gori']:
                if self.DB['new_gori'][_].find(self.ui.lineEdit.text()) != -1:
                    self.ui.out_list.append(_)

    def cal_function(self):
        self.ui.out_pro.clear()
        temp = self.ui.textEdit.toPlainText()

        layer = [self.ui.val_1_1, self.ui.val_1_2, self.ui.val_1_3, self.ui.val_1_4, self.ui.val_1_5, self.ui.val_1_6,
                 self.ui.val_1_7, self.ui.val_1_8, self.ui.val_1_9, self.ui.val_1_10, self.ui.val_1_11,
                 self.ui.val_1_12, self.ui.val_1_13, self.ui.val_1_14, self.ui.val_1_15, self.ui.val_1_16]
        cont = ['조절', '조치', '수행', '전환', '재설정', '복구', '충수', '차단', '배기', '기동', '시도', '사용',
                '정지', '실시', '유지', '시작']

        tot = 0
        for _ in range(len(layer)):
            layer[_].setText('{} : {}'.format(cont[_], temp.count(cont[_])))
            tot += temp.count(cont[_])
        self.ui.label_4.setText('- 제어관련 - : {}'.format(tot))

        layer = [self.ui.val_2_1, self.ui.val_2_2, self.ui.val_2_3, self.ui.val_2_4, self.ui.val_2_5]
        cont = ['확인', '점검', '평가', '감시', '발생']

        tot = 0
        for _ in range(len(layer)):
            layer[_].setText('{} : {}'.format(cont[_], temp.count(cont[_])))
            tot += temp.count(cont[_])
        self.ui.label_2.setText('- 감시관련 - : {}'.format(tot))

        ##
        line = temp.split('\n')
        for _ in line:
            if '비정상' in _:
                self.ui.out_pro.append(_)


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())