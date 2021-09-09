import sys
from MyBudIdentify_Pane import MyBudIdentifyPane
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    budIdentify = MyBudIdentifyPane()
    budIdentify.show()
    # #*****************自定义信号槽start*************#
    # def getSrc(file_path):
    #     print(file_path)
    #     self.label.setText(file_path)
    #*****************自定义信号槽end***************#

    sys.exit(app.exec_())