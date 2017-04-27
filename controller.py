# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QTimer
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(727, 338)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.currentModeText = QtGui.QTextBrowser(self.centralwidget)
        self.currentModeText.setGeometry(QtCore.QRect(160, 60, 151, 31))
        self.currentModeText.setObjectName(_fromUtf8("currentModeText"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.modeSelectComboBox = QtGui.QComboBox(self.centralwidget)
        self.modeSelectComboBox.setGeometry(QtCore.QRect(160, 110, 151, 31))
        self.modeSelectComboBox.setObjectName(_fromUtf8("modeSelectComboBox"))
        self.modeSelectComboBox.insertItem(0,_fromUtf8("连续波"))
        self.modeSelectComboBox.insertItem(0,_fromUtf8("断续波"))
        self.modeSelectComboBox.insertItem(0,_fromUtf8("疏密波"))
        
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 180, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lastTimeDisplay = QtGui.QLCDNumber(self.centralwidget)
        self.lastTimeDisplay.setGeometry(QtCore.QRect(160, 160, 151, 41))
        self.lastTimeDisplay.setObjectName(_fromUtf8("lastTimeDisplay"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(250, 220, 81, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(390, 220, 81, 31))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 60, 41, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 110, 61, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 180, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frequencyInputText = QtGui.QTextEdit(self.centralwidget)
        self.frequencyInputText.setGeometry(QtCore.QRect(500, 60, 101, 31))
        self.frequencyInputText.setObjectName(_fromUtf8("frequencyInputText"))
        self.pulseWidthInputText = QtGui.QTextEdit(self.centralwidget)
        self.pulseWidthInputText.setGeometry(QtCore.QRect(500, 110, 101, 31))
        self.pulseWidthInputText.setObjectName(_fromUtf8("pulseWidthInputText"))
        self.timeSetInputText = QtGui.QTextEdit(self.centralwidget)
        self.timeSetInputText.setGeometry(QtCore.QRect(500, 170, 101, 31))
        self.timeSetInputText.setObjectName(_fromUtf8("timeSetInputText"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 70, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 120, 54, 12))
        self.label_8.setLineWidth(3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 180, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.timer = QTimer(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.runningMode=2
        self.modeSelectComboBox.setCurrentIndex(self.runningMode)
        self.runningModeMap={3:_fromUtf8(""),2:_fromUtf8("连续波"),1:_fromUtf8("断续波"),0:_fromUtf8("疏密波")}
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "当前状况", None))
        self.label_2.setText(_translate("MainWindow", "模式选择", None))
        self.label_3.setText(_translate("MainWindow", "剩余时间", None))
        self.startButton.setText(_translate("MainWindow", "启动", None))
        self.stopButton.setText(_translate("MainWindow", "暂停", None))
        self.label_4.setText(_translate("MainWindow", "频  率", None))
        self.label_5.setText(_translate("MainWindow", "波间距", None))
        self.label_6.setText(_translate("MainWindow", "定时设置", None))
        self.label_7.setText(_translate("MainWindow", "HZ", None))
        self.label_8.setText(_translate("MainWindow", "MS", None))
        self.label_9.setText(_translate("MainWindow", "S", None))
        self.timer.timeout.connect(self.timeoutInturrupt)
        self.timer.start(1000) 
        self.startButton.clicked.connect(self.startButtonEvent)
        self.stopButton.clicked.connect(self.stopButtonEvent)
        self.modeSelectComboBox.currentIndexChanged.connect(self.modeSelectChange)
        self.remainTime=60
        self.run=False
    def startButtonEvent(self):
        timeSetText=self.timeSetInputText.toPlainText()
        try:
            self.remainTime=int(timeSetText)
            self.run=True
        except:
            self.alarmInfo(_fromUtf8("Time paramter incorrect!"))
            self.remainTime=0
            self.run=False
        self.lastTimeDisplay.display(self.remainTime)
        pass
    def stopButtonEvent(self):
        pass
    def alarmInfo(self,words):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(str(words))
        msgBox.exec_()
    def timeoutInturrupt(self):
        self.currentModeText.setText(self.runningModeMap[self.runningMode])# 设置 当前状况 信息
        if(self.run and self.remainTime!=0):
            self.remainTime-=1
            self.lastTimeDisplay.display(self.remainTime)
        elif(self.run and self.remainTime==0):
            self.run=False
    def modeSelectChange(self):
        self.runningMode=self.modeSelectComboBox.currentIndex()

    def setParameter(self):
        print "Serial send parameter:",
        if(self.runningMode==2):#连续波
            pass
        elif(self.runningMode==1):#断续波
            pass
        elif(self.runningMode==0):#疏密波
            pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HelloPyQt = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(HelloPyQt)
    HelloPyQt.show()
sys.exit(app.exec_())