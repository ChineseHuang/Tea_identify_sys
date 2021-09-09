from login_pane import LoginPane
from register_pane import RegisterPane
from MyBudIdentify_Pane import MyBudIdentifyPane
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QPropertyAnimation,QAbstractAnimation,QEasingCurve
from PyQt5.QtWidgets import QErrorMessage,QMessageBox
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pane = LoginPane()    #登录面板
    register_pane = RegisterPane(login_pane)    #注册面板
    budIdentify = MyBudIdentifyPane()

    register_pane.move(0,register_pane.height())
    register_pane.show()
    #******************自定义信号的槽函数start***************************#
    #退出注册界面槽
    def exit_register_pane():
        register_pane.move(0,register_pane.height())
    #注册用户槽
    def register_account():
        pass
    #弹出注册界面槽
    def show_register_pane():
        register_pane.move(0, 0)
    #检查登录信息
    def check_login(account,pwd):
        if account=='laixiaoyi' and pwd=='123':
            print('登录成功')
            budIdentify.show()  #展示茶叶嫩芽识别系统界面
            login_pane.deleteLater()    #销毁登录界面
        else:
            print('登陆失败')
            login_pane.show_error_antimation()
            em = QErrorMessage(login_pane)
            em.showMessage('密码错误')
            em.open()

    #******************自定义信号的槽函数end**************************************#
    #信号连接
    #退出注册界面信号
    register_pane.exit_signal.connect(exit_register_pane)
    #注册信号
    register_pane.register_signal.connect(register_account)
    #弹出注册界面信号
    login_pane.show_register_pane_signal.connect(show_register_pane)
    #检查登录信号
    login_pane.check_login_signal.connect(check_login)
    login_pane.show()
    sys.exit(app.exec_())