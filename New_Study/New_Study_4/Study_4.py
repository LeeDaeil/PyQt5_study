from PySide2.QtWidgets import  (QDialog, QCheckBox, QPushButton, QToolButton,
                                QListWidget, QListWidgetItem, QLabel, QTreeWidget, QTreeWidgetItem,
                                QVBoxLayout, QHBoxLayout)
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt

#import ActiveSet_rc

class ActiveSetDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        showSetCB = QCheckBox("Show SelectedSet")
        applyPB = QPushButton("&Apply")
        closePB = QPushButton("&Close")

        toActiveTB = QToolButton()
        toActiveTB.setIcon(QIcon(":/images/forward.png"))
        toActiveTB.setIconSize(QSize(32,32))
        toActiveTB.setAutoRaise(True)

        toInactiveTB = QToolButton()
        toInactiveTB.setIcon(QIcon(":/images/backward.png"))
        toInactiveTB.setIconSize(QSize(32,32))
        toInactiveTB.setAutoRaise(True)

        self.inactiveSetLW = QListWidget()
        self.inactiveSetLW.setAlternatingRowColors(True)

        self.inactiveSetLW.addItem("Set 1")
        self.inactiveSetLW.addItem("Set 2")
        self.inactiveSetLW.addItem("Set 3")
        self.inactiveSetLW.addItem("Set 4")

        self.activeSetLW = QListWidget()
        self.activeSetLW.setAlternatingRowColors(True)

        self.activeSetLW.addItem("Set 10")
        self.activeSetLW.addItem("Set 11")
        self.activeSetLW.addItem("Set 12")

        inactiveLabel = QLabel("Inactive Set")
        activeLabel = QLabel("Active Set")

        left = QVBoxLayout()
        left.addWidget(inactiveLabel)
        left.addWidget(self.inactiveSetLW)

        center = QVBoxLayout()
        center.addStretch()
        center.addWidget(toActiveTB)
        center.addWidget(toInactiveTB)
        center.addStretch()

        right = QVBoxLayout()
        right.addWidget(activeLabel)
        right.addWidget(self.activeSetLW)

        top = QHBoxLayout()
        top.addLayout(left)
        top.addLayout(center)
        top.addLayout(right)

        bottom = QHBoxLayout()
        bottom.addWidget(showSetCB)
        bottom.addStretch()
        bottom.addWidget(applyPB)
        bottom.addWidget(closePB)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(top)
        mainLayout.addLayout(bottom)

        self.setLayout(mainLayout)

        # drag-drop setting
        self.inactiveSetLW.setDragEnabled(True)
        self.inactiveSetLW.viewport().setAcceptDrops(True)
        self.inactiveSetLW.setDropIndicatorShown(True)
        self.inactiveSetLW.setDefaultDropAction(Qt.MoveAction)

        self.activeSetLW.setDragEnabled(True)
        self.activeSetLW.viewport().setAcceptDrops(True)
        self.activeSetLW.setDropIndicatorShown(True)
        self.activeSetLW.setDefaultDropAction(Qt.MoveAction)

        # signal-slot
        closePB.clicked.connect(self.close)
        toActiveTB.clicked.connect(self.onToActiveSet)
        toInactiveTB.clicked.connect(self.onToInactiveSet)

    def onToActiveSet(self):
        self.moveCurrentItem(self.inactiveSetLW,self.activeSetLW)

    def onToInactiveSet(self):
        self.moveCurrentItem(self.activeSetLW,self.inactiveSetLW)

    def moveCurrentItem(self,source,target):

        if source.currentItem() :
            row = source.currentRow()
            target.addItem(source.takeItem(row))


from PySide2.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = ActiveSetDialog()
    dialog.show()

    app.exec_()