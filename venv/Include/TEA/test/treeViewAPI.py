import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = QDirModel()   #window系统提供的模式
    tree = QTreeView()
    tree.setModel(model)
    tree.setWindowTitle('文件导航目录')
    tree.resize(600,600)
    tree.show()
    sys.exit(app.exec_())