import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QRadioButton,QCheckBox,QCommandLinkButton,QAction,QMenu,QToolButton,QToolTip
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QObject,QPoint,pyqtSignal
from resource.caculator_ui import Ui_Form


class Caculator(QObject):
    #自定义信号
    show_content = pyqtSignal(str)

    def __init__(self,parent):
        super().__init__(parent)
        #num数字键，operator操作键，equal计算键，clear归零键
        self.content = ''
        self.key_models = []

    def caculate(self):
        #计算结果
        expression = ''
        if self.key_models[-1]['role'] == 'operator':
            self.key_models.pop(-1)
        for key in self.key_models:
            expression += key['title']
        result = eval(expression)
        print(result)
        return result

    def parse_key_model(self,key_model):
        #处理按键
        #按下归零键
        if key_model['role'] == 'clear':
            print('归零')
            self.show_content.emit('0.0')
            self.key_models = []
            return None
        if key_model['role'] == 'caculate':
            print('计算结果')
            if len(self.key_models) > 0:
                result = self.caculate()
                self.show_content.emit(str(result))
            self.key_models = []
            return None
        #输入算术公式
        #第一个输入必须为数字键
        if len(self.key_models)==0:
            if key_model['role'] == 'num':
                if key_model['title'] != '.':
                    self.key_models.append(key_model)
                    self.show_content.emit(key_model['title'])
            print(self.key_models)
            return None
        #如果输入=/-和%号
        if key_model['title'] in ('%','+/-'):
            if self.key_models[-1]['role'] == 'num':
                if key_model['title'] == '%':
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title'])/100) #如果是%，则把数字转换为小数
                else:
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title'])*-1)
                return None
            else:
                return None
        # 之后输入的键位和前一个键位类型相同
        if self.key_models[-1]['role'] == key_model['role']:
            #如果都是数字键
            if key_model['role'] == 'num':
                #如果输入的是小数点，则需判断前面是否含有小数点
                if key_model['title'] == '.' and self.key_models[-1]['title'].__contains__('.'):
                    return None
                #如果输入的数字是0
                if self.key_models[-1]['title'] == '0':
                    self.key_models[-1]['title'] = key_model['title']
                else:
                    self.key_models[-1]['title'] += key_model['title']
            #如果是操作键
            if key_model['role'] == 'operator':
                self.key_models[-1]['title'] = key_model['title']
        else:
            self.key_models.append(key_model)

        # 把每次输入符合条件的都存入key_models中
        # 按下计算键
        print(self.key_models)

class CaculatorPane(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)  #显示背景图
        self.setupUi(self)
        self.caculator = Caculator(self)
        self.caculator.show_content.connect(self.show_content)

    def show_content(self,content):
        self.lineEdit.setText(content)

#*********************槽函数start**********************************#
    #获取按下的键位，交给caculator类处理
    def get_key(self,title,role):
        self.caculator.parse_key_model({'title':title,'role':role})
#*********************槽函数end**********************************#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaculatorPane()
    window.show()
    sys.exit(app.exec_())

