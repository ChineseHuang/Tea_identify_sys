import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2

#图片显示和操作
class ImageView(QGraphicsView):

    def __init__(self,parent=None,*args):
        super().__init__(parent,*args)
        self.imageScale = 0.1       #图像显示的比例

    def showImage(self,file_path):
        self.imageScale = 0.1
        pix = QPixmap(file_path)
        self.item = QGraphicsPixmapItem(pix)     #创建图元
        self.item.setScale(self.imageScale)
        sence = QGraphicsScene()    #创建场景
        sence.addItem(self.item) #将图元加入场景中
        self.setScene(sence)    #将场景加入视图中

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    iv = ImageView(win)
    win.resize(600,600)
    win.setWindowTitle('图像显示')
    iv.resize(600,600)
    iv.showImage('D://code//pythonCode//Tea_Identify//venv//Include//TEA//girl.jpg')
    win.show()
    sys.exit(app.exec_())