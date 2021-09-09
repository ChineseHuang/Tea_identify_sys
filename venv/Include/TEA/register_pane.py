import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QRadioButton,QCheckBox,QCommandLinkButton,QAction,QMenu,QToolButton,QToolTip
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt,QObject,QPoint,QAbstractAnimation,QSequentialAnimationGroup,QPropertyAnimation,pyqtSignal
# from PyQt5 import QtWidgets,QtGui,QtCore,Qt
from resource.register_ui import Ui_Form
# import images_rc
#

class RegisterPane(QWidget,Ui_Form):
    #自定义信号,registerPane的信号
    exit_signal = pyqtSignal()  #退出信号
    register_signal = pyqtSignal(str,str) #注册信号
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)  #显示背景图
        self.setupUi(self)
        self.antimate_target = [self.regAboutBtn,self.regResetBtn,self.regExitBtn]  #设置动画组对象
        # self.antimate_target_pos = [target.pos() for target in self.antimate_target]
        self.antimate_target_pos = [QPoint(90, 0),QPoint(70, 60),QPoint(0, 80)]

    def show_hide_btn(self,checked):
        print('菜单',checked)
        antimate_group = QSequentialAnimationGroup(self )
        for i,btn in enumerate(self.antimate_target,0):
            antimate = QPropertyAnimation()
            antimate.setTargetObject(btn)
            antimate.setPropertyName(b'pos')
            antimate.setStartValue(self.regMenuBtn.pos())
            antimate.setEndValue(self.antimate_target_pos[i])
            antimate.setDuration(200)
            antimate_group.addAnimation(antimate)
        if not checked:
            antimate_group.setDirection(QAbstractAnimation.Backward)
        antimate_group.start(QAbstractAnimation.DeleteWhenStopped)


    def about(self):
        print('关于')
        QMessageBox.about(self,'茶叶嫩芽识别系统','识别嫩芽图像')

    def reset(self):
        print('重置')
        self.AccountEdit.clear()
        self.PasswordEdit.clear()
        self.ensurePwdEdit.clear()

    def btn_exit(self):
        self.exit_signal.emit() #向外界发射退出信号

    def register(self):
        account_txt = self.AccountEdit.text()
        pwd_txt = self.PasswordEdit.text()
        self.register_signal.emit(account_txt,pwd_txt)   #向外界发射注册信号

    def registerBtnEnable(self):
        print('判定')
        account_txt = self.AccountEdit.text()
        pwd_txt = self.PasswordEdit.text()
        confirm_txt = self.ensurePwdEdit.text()
        if len(account_txt)>0 and len(pwd_txt)>0 and len(confirm_txt)>0 and pwd_txt==confirm_txt:
            self.registerBtn.setEnabled(True)
        else:
            self.registerBtn.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda : print('我退出了'))
    window.register_signal.connect(lambda account,pwd: print(account,pwd))
    window.show()
    sys.exit(app.exec_())

