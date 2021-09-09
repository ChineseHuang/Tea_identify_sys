import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QRadioButton,QCheckBox,QCommandLinkButton,QAction,QMenu,QToolButton,QToolTip
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QObject,QPoint,pyqtSignal

#
class CaculatorButton(QPushButton):
    #自定义信号
    key_pressed = pyqtSignal(str,str)   #自定义按钮点击信号，同时传递消息

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.key_pressed.emit(self.text(),self.property('role'))    #发射信号

    def __init__(self,*args):
        super().__init__(*args)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setStyleSheet("""
        QPushButton[bg]{
            font: 24px "楷体";
            background-color:orange;
            border-radius:%dpx;
        }
        QPushButton[bg='gray']{
            color:white;
            background-color:rgb(88,88,88);
        }
        QPushButton[bg='gray']:hover{
            background-color:rgb(150,150,150);
        }
        QPushButton[bg='orange'],QPushButton[bg='equal']{
            color:white;
            background-color:rgb(207,138,0);
        }
        QPushButton[bg='orange']:hover,QPushButton[bg='equal']:hover{
            background-color:rgb(238,159,0);
        }
        QPushButton[bg='orange']:checked{
            background-color:white;
            color:rgb(207,138,0);
        }
        QPushButton[bg='lightgray']{
            color:black;
            background-color:rgb(200,200,200);
        }
        QPushButton[bg='lightgray']:hover{
            color:white;
            background-color:rgb(230,230,230);
        }
        """ % (min(self.width(), self.height()) // 2))