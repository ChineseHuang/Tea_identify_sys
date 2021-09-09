import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QRadioButton,QCheckBox,QCommandLinkButton,QAction,QMenu,QToolButton,QToolTip
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtCore import QPropertyAnimation,QAbstractAnimation,Qt,QObject,QPoint,QSize,pyqtSignal,QUrl
from resource.login_ui import Ui_Form



class LoginPane(QWidget,Ui_Form):
    show_register_pane_signal = pyqtSignal()    #注册界面弹出信号
    check_login_signal = pyqtSignal(str,str)    #检查登录信息信号

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)  #显示背景图
        self.setupUi(self)
        #加载动图
        # movie = QMovie('::/login/images/嫩芽动图.gif')
        # movie.setScaledSize(QSize(500,111))
        # self.loginTopBgLabel.setMovie(movie)
        # movie.start()

    #打开注册界面槽
    def show_register_pane(self):
        self.show_register_pane_signal.emit()   #向外界发射注册信号界面

    #打开外部链接槽
    def open_link(self):
        #打开一个连接
        print('百度')
        url = 'https://www.baidu.com/'
        print('你好')
        QDesktopServices.openUrl(QUrl(url))

#*********************槽函数start**********************************#
    #监听输入框文本，如果都有文本则会启用登录按钮
    def enable_login_btn(self):
        account_txt = self.accountCb.currentText()
        pwd_txt = self.pwdEdit.text()
        if len(account_txt)>0 and len(pwd_txt)>0:
            self.loginBtn.setEnabled(True)
        else:
            self.loginBtn.setEnabled(False)

    #检查登录信息
    def check_login(self):
        #检查登录信息，如果正确则登录
        account_txt = self.accountCb.currentText()
        pwd_txt = self.pwdEdit.text()
        self.check_login_signal.emit(account_txt,pwd_txt)   #想外部发射检查登录信息的信号

    #自动登录
    def auto_login(self,checked):
        print('自动登录',checked)
        if checked:
            self.remmeberPwdCb.setChecked(True)

    #记住密码
    def remember_pwd(self,checked):
        print('记住密码',checked)
        if not checked:
            self.autoLoginCb.setChecked(True)

# *********************槽函数end**********************************#

    #登录信息错误动画
    def show_error_antimation(self):
        antimation = QPropertyAnimation(self)
        antimation.setTargetObject(self.loginBottom)
        antimation.setPropertyName(b'pos')
        antimation.setKeyValueAt(0,self.loginBottom.pos())
        antimation.setKeyValueAt(0.2,self.loginBottom.pos()+QPoint(15,0))
        antimation.setKeyValueAt(0.5,self.loginBottom.pos())
        antimation.setKeyValueAt(0.7,self.loginBottom.pos()+QPoint(-15,0))
        antimation.setKeyValueAt(0.1,self.loginBottom.pos())
        antimation.setDuration(100)
        antimation.setLoopCount(3)
        antimation.start(QAbstractAnimation.DeleteWhenStopped)

    #登录失败弹出提示框
    def show_error_dialog(self):
        em = QErrorMessage(self)
        em.showMessage('密码错误')
        em.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())

