import sys
import cv2

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    img = cv2.imread('girl.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = img.shape[1]
    y = img.shape[0]
    app = QApplication(sys.argv)
    print('1')
    win = QWidget()
    win.setWindowTitle('显示图像')
    win.resize(600,600)
    print('2')
    picshow = QGraphicsView(win)
    picshow.resize(500,500)
    print('3')
    frame = QImage(img,x,y,QImage.Format_BGR888)
    print('4')
    pix = QPixmap.fromImage(frame)
    print('5')
    item = QGraphicsPixmapItem(pix)
    scene = QGraphicsScene()
    scene.addItem(item)
    picshow.setScene(scene)
    win.show()
    sys.exit(app.exec_())



