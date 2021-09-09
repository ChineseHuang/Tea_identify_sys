import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#文件导航目录
class FileBrowser(QTreeView):
    #自定义信号
    sendSrc = pyqtSignal(str,str)
    def __init__(self,parent=None,*args):
        super().__init__(parent,*args)
        self.model = QDirModel()
        self.setModel(self.model)
        self.setRootIndex(self.model.index(r'D:\个人文件\学术\数据\新茶叶数据-张蕴'))
        self.doubleClicked.connect(self.file_name) #双击文件打开

    def file_name(self, modelIndex ):
        file_path = self.model.filePath(modelIndex)
        file_name = self.model.fileName(modelIndex)
        self.sendSrc.emit(file_path,file_name)
        print(self.model.fileName(modelIndex))  # 输出文件名


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fb = FileBrowser()
    fb.setWindowTitle('文件目录')
    fb.resize(600,600)
    fb.show()
    sys.exit(app.exec_())