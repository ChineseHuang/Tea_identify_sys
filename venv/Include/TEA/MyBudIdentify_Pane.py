import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from resource.MyBudIdentify_ui import Ui_mainWindow
import MyLabelImg
import os.path
import argparse

class MyBudIdentifyPane(QWidget,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        #MainWindow的初始化参数
        # argparser = argparse.ArgumentParser()
        # argparser.add_argument("image_dir", nargs="?")
        # argparser.add_argument("class_file",
        #                        default=os.path.join(os.path.dirname(__file__), "data", "predefined_classes.txt"),
        #                        nargs="?")
        # argparser.add_argument("save_dir", nargs="?")
        # args = argparser.parse_args(sys.argv[1:])
        # args.image_dir = args.image_dir and os.path.normpath(args.image_dir)
        # args.class_file = args.class_file and os.path.normpath(args.class_file)
        # args.save_dir = args.save_dir and os.path.normpath(args.save_dir)
        #MainWindow的初始化参数
        
        self.setAttribute(Qt.WA_StyledBackground,True)  #显示背景图
        self.setupUi(self)
        self.currentImage_path = ''     #存储当前显示的文件的路径
        
        # #添加图片标注控件
        # self.imageAnnotation = MainWindow(args.image_dir,
        #              args.class_file,
        #              args.save_dir)
        # self.imageAnnotation.setParent(self.imageAnnotationTab)
        # self.imageAnnotation.setGeometry(0,0,1096,792)

    #****************槽函数start***************************#
    #获取文件路径
    def getSrc(self,file_path,file_name):
        file_path = file_path.replace(r'/',r'//')
        self.currentImage_path = file_path
        print(self.currentImage_path)
        self.label.setText(file_name)
        self.pictureShow.showImage(file_path)

    #图像操作
    #裁剪
    def imageCut(self):
        print('裁剪')

    #镜像
    def imageMirror(self):
        print('镜像')

    #放大
    def imageBigger(self):
        print('放大')
        self.pictureShow.imageScale += 0.05
        if self.pictureShow.imageScale >= 1.5:
            self.pictureShow.imageScale = 1.5
        self.pictureShow.item.setScale(self.pictureShow.imageScale) #重设图片显示比例

    #缩小
    def imageSmaller(self):
        print('缩小')

    #旋转
    def imageRatate(self):
        print('旋转')

    #直方图均衡化
    def imageAnnotation(self):
        print('图像标注')
        MyLabelImg.create()

        
        
    #***************槽函数end******************************#
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyBudIdentifyPane()
    window.show()
    sys.exit(app.exec_())

