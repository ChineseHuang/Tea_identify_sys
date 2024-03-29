# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyBudIdentify.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1100, 850)
        mainWindow.setMinimumSize(QtCore.QSize(1100, 850))
        mainWindow.setMaximumSize(QtCore.QSize(1100, 850))
        mainWindow.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(mainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 850))
        self.tabWidget.setMinimumSize(QtCore.QSize(1100, 850))
        self.tabWidget.setMaximumSize(QtCore.QSize(1100, 850))
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
"    border: 2px solid rgb(210, 210, 210);\n"
"    background:rgb(246, 246, 246);\n"
"    border-top-color:transparent;\n"
"}\n"
"QTabWidget::tab-bar{\n"
"    background:rgb(0, 0, 0);\n"
"    subcontrol-position:left;\n"
"}\n"
"QTabBar::tab{\n"
"    font: 20pt \"楷体\";\n"
"    width:150px;\n"
"    height:50px;\n"
"    background-color: rgb(170, 255, 0);\n"
"    border: 2px solid rgb(210, 210, 210);\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"QTabBar::tab:selected{    \n"
"    background:rgb(246, 246, 246);\n"
"    border-bottom-color:rgb(246, 246, 246);\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(440, 320, 251, 91))
        self.pushButton.setStyleSheet("font: 36pt \"楷体\";\n"
"background-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.imageProcessTab = QtWidgets.QWidget()
        self.imageProcessTab.setObjectName("imageProcessTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.imageProcessTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.imageProcessTab)
        self.widget.setObjectName("widget")
        self.fileBrowser = FileBrowser(self.widget)
        self.fileBrowser.setGeometry(QtCore.QRect(0, 11, 211, 751))
        self.fileBrowser.setObjectName("fileBrowser")
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.imageProcessTab)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cutBtn = QtWidgets.QPushButton(self.widget_3)
        self.cutBtn.setObjectName("cutBtn")
        self.horizontalLayout_2.addWidget(self.cutBtn)
        self.mirrorBtn = QtWidgets.QPushButton(self.widget_3)
        self.mirrorBtn.setObjectName("mirrorBtn")
        self.horizontalLayout_2.addWidget(self.mirrorBtn)
        self.biggerBtn = QtWidgets.QPushButton(self.widget_3)
        self.biggerBtn.setObjectName("biggerBtn")
        self.horizontalLayout_2.addWidget(self.biggerBtn)
        self.smallerBtn = QtWidgets.QPushButton(self.widget_3)
        self.smallerBtn.setObjectName("smallerBtn")
        self.horizontalLayout_2.addWidget(self.smallerBtn)
        self.ratateBtn = QtWidgets.QPushButton(self.widget_3)
        self.ratateBtn.setObjectName("ratateBtn")
        self.horizontalLayout_2.addWidget(self.ratateBtn)
        self.annotationBtn = QtWidgets.QPushButton(self.widget_3)
        self.annotationBtn.setObjectName("annotationBtn")
        self.horizontalLayout_2.addWidget(self.annotationBtn)
        self.verticalLayout.addWidget(self.widget_3)
        self.pictureShow = ImageView(self.widget_2)
        self.pictureShow.setObjectName("pictureShow")
        self.verticalLayout.addWidget(self.pictureShow)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 20pt \"楷体\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 24)
        self.verticalLayout.setStretch(2, 2)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        self.tabWidget.addTab(self.imageProcessTab, "")
        self.modelTrainTab = QtWidgets.QWidget()
        self.modelTrainTab.setObjectName("modelTrainTab")
        self.tabWidget.addTab(self.modelTrainTab, "")
        self.budIdentifyTab = QtWidgets.QWidget()
        self.budIdentifyTab.setObjectName("budIdentifyTab")
        self.tabWidget.addTab(self.budIdentifyTab, "")

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.fileBrowser.sendSrc.connect(mainWindow.getSrc)
        self.ratateBtn.clicked.connect(mainWindow.imageRatate)
        self.cutBtn.clicked.connect(mainWindow.imageCut)
        self.mirrorBtn.clicked.connect(mainWindow.imageMirror)
        self.biggerBtn.clicked.connect(mainWindow.imageBigger)
        self.smallerBtn.clicked.connect(mainWindow.imageSmaller)
        self.annotationBtn.clicked.connect(mainWindow.imageAnnotation)
        self.pushButton.clicked.connect(mainWindow.imageAnnotation)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "嫩芽识别系统"))
        self.pushButton.setText(_translate("mainWindow", "图像标注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "图像标注"))
        self.cutBtn.setText(_translate("mainWindow", "裁剪"))
        self.mirrorBtn.setText(_translate("mainWindow", "镜像"))
        self.biggerBtn.setText(_translate("mainWindow", "放大"))
        self.smallerBtn.setText(_translate("mainWindow", "缩小"))
        self.ratateBtn.setText(_translate("mainWindow", "旋转"))
        self.annotationBtn.setText(_translate("mainWindow", "图像标注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageProcessTab), _translate("mainWindow", "图像处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modelTrainTab), _translate("mainWindow", "模型训练"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.budIdentifyTab), _translate("mainWindow", "嫩芽识别"))
from MyFileBrowser import FileBrowser
from MyImageView import ImageView
