# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports

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
        self.label.setGeometry(QtCore.QRect(90, 170, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.currentModeText = QtGui.QTextBrowser(self.centralwidget)
        self.currentModeText.setGeometry(QtCore.QRect(160, 180, 201, 31))
        self.currentModeText.setObjectName(_fromUtf8("currentModeText"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.modeSelectComboBox = QtGui.QComboBox(self.centralwidget)
        self.modeSelectComboBox.setGeometry(QtCore.QRect(160, 70, 151, 31))
        self.modeSelectComboBox.setObjectName(_fromUtf8("modeSelectComboBox"))
        self.modeSelectComboBox.insertItem(0,_fromUtf8("连续波"))
        self.modeSelectComboBox.insertItem(0,_fromUtf8("断续波"))
        self.modeSelectComboBox.insertItem(0,_fromUtf8("疏密波"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 130, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lastTimeDisplay = QtGui.QLCDNumber(self.centralwidget)
        self.lastTimeDisplay.setGeometry(QtCore.QRect(160, 120, 121, 31))
        self.lastTimeDisplay.setObjectName(_fromUtf8("lastTimeDisplay"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(250, 250, 81, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(390, 250, 81, 31))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 20, 41, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 70, 61, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 130, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 30, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 80, 54, 12))
        self.label_8.setLineWidth(3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 130, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 30, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_pwm = QtGui.QLabel(self.centralwidget)
        self.label_pwm.setGeometry(QtCore.QRect(418, 180, 54, 12))
        self.label_pwm.setObjectName(_fromUtf8("label_pwm"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 180, 54, 12))#debug
        self.label_11.setObjectName(_fromUtf8("label_pwm"))
        self.text_pwm = QtGui.QLineEdit(self.centralwidget)
        self.text_pwm.setGeometry(QtCore.QRect(500, 170, 101, 31))
        self.text_pwm.setObjectName(_fromUtf8("text_pwm"))
        self.comSelect = QtGui.QComboBox(self.centralwidget)
        self.comSelect.setGeometry(QtCore.QRect(160, 20, 69, 22))
        self.comSelect.setObjectName(_fromUtf8("comSelect"))
        self.frequencyInputText = QtGui.QLineEdit(self.centralwidget)
        self.frequencyInputText.setGeometry(QtCore.QRect(500, 19, 101, 31))
        self.frequencyInputText.setObjectName(_fromUtf8("frequencyInputText"))
        self.pulseWidthInputText = QtGui.QLineEdit(self.centralwidget)
        self.pulseWidthInputText.setGeometry(QtCore.QRect(500, 70, 101, 31))
        self.pulseWidthInputText.setObjectName(_fromUtf8("pulseWidthInputText"))
        self.timeSetInputText = QtGui.QLineEdit(self.centralwidget)
        self.timeSetInputText.setGeometry(QtCore.QRect(500, 120, 101, 31))
        self.timeSetInputText.setObjectName(_fromUtf8("timeSetInputText"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)



        self.timer = QTimer(self.centralwidget)
        self.timer_100ms=QTimer(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pulseWidth=100
        self.frequency=50
        self.pwm=50
        self.frequencyInputText.setText(str(self.frequency))
        self.pulseWidthInputText.setText(str(self.pulseWidth))
        self.text_pwm.setText(str(self.pwm))
        self.timeSetInputText.setText("120")
        self.runningMode=2
        self.modeSelectComboBox.setCurrentIndex(self.runningMode)
        self.runningModeMap={3:_fromUtf8(""),2:_fromUtf8("连续波"),1:_fromUtf8("断续波"),0:_fromUtf8("疏密波")}
        #Detect serial devices
        self.deviceBaud=19200#串口通信波特率
        self.currentComs=set()
        self.currentComsMap={}
        self.currentComSelect=""
        serialLists=list(serial.tools.list_ports.comports())
        comboxCount=0
        if(len(serialLists)!=0):
            for serialInfo in serialLists:
                serialName=serialInfo[0]
                self.currentComs.add(serialName)
                self.currentComsMap[comboxCount]=serialName
                self.comSelect.insertItem(comboxCount,_fromUtf8(serialName))
                comboxCount+=1
            self.currentComSelect=serialLists[0][0]
            self.comSelect.setCurrentIndex(0)
            self.device=serial.Serial(self.currentComSelect,self.deviceBaud)#更改设备串口号
        else:
            self.comSelect.insertItem(0,_fromUtf8(""))
        
        self.timer.timeout.connect(self.timeoutInturrupt)
        self.timer_100ms.timeout.connect(self.timeoutInturrupt_100ms)
        self.timer.start(1000) 
        self.timer_100ms.start(100) 
        self.startButton.clicked.connect(self.startButtonEvent)
        self.stopButton.clicked.connect(self.stopButtonEvent)
        self.frequencyInputText.returnPressed.connect(self.frequencyChange)
        self.pulseWidthInputText.returnPressed.connect(self.pulsewidthChange)
        self.text_pwm.returnPressed.connect(self.pwmChange)
        self.modeSelectComboBox.currentIndexChanged.connect(self.modeSelectChange)
        self.comSelect.currentIndexChanged.connect(self.deviceSelectChange)
        self.remainTime=60
        self.run=False

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "当前状态", None))
        self.label_2.setText(_translate("MainWindow", "模式选择", None))
        self.label_3.setText(_translate("MainWindow", "剩余时间", None))
        self.startButton.setText(_translate("MainWindow", "启动", None))
        self.stopButton.setText(_translate("MainWindow", "暂停", None))
        self.label_4.setText(_translate("MainWindow", "频  率", None))
        self.label_5.setText(_translate("MainWindow", "脉宽", None))
        self.label_6.setText(_translate("MainWindow", "定时设置", None))
        self.label_7.setText(_translate("MainWindow", "HZ", None))
        self.label_8.setText(_translate("MainWindow", "us", None))
        self.label_9.setText(_translate("MainWindow", "S", None))
        self.label_10.setText(_translate("MainWindow", "端口号", None))
        self.label_pwm.setText(_translate("MainWindow", "占空比", None))
        self.label_11.setText(_translate("MainWindow", "%", None))

    def startButtonEvent(self):
        if(self.startButton.text()==u"启动"):
            timeSetText=self.timeSetInputText.text()
            try:
                self.remainTime=int(timeSetText)
                self.run=True
            except:
                self.alarmInfo(_fromUtf8("Time paramter incorrect!"))
                self.remainTime=0
                self.run=False
            self.lastTimeDisplay.display(self.remainTime)
            self.startButton.setText(_translate("MainWindow", "终止", None))
            self.setParameter(True)#True表示启动 #False表示停止
        elif(self.startButton.text()==u"终止"):
            self.run=False
            self.remainTime=0
            self.lastTimeDisplay.display(self.remainTime)
            self.startButton.setText(_translate("MainWindow", "启动", None))
            self.stopButton.setText(_translate("MainWindow", "暂停", None))
            self.setParameter(False)#True表示启动 #False表示停止

    def stopButtonEvent(self):
        if(self.stopButton.text()==u"暂停" and self.run==True):
            self.stopButton.setText(_translate("MainWindow", "继续", None))
            self.run=False
            self.setParameter(False)#True表示启动 #False表示停止
        elif(self.stopButton.text()==u"继续" and self.run==False):
            self.stopButton.setText(_translate("MainWindow", "暂停", None))
            self.run=True
            self.setParameter(True)#True表示启动 #False表示停止

    def alarmInfo(self,words):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(str(words))
        msgBox.exec_()

    def timeoutInturrupt(self):#1S发生一次中断
        if(self.run and self.remainTime!=0):
            self.remainTime-=1
            self.lastTimeDisplay.display(self.remainTime)
        elif(self.run and self.remainTime==0):
            self.setParameter(False)#True表示启动 #False表示停止
            self.run=False
            self.startButton.setText(_translate("MainWindow", "启动", None))
            self.stopButton.setText(_translate("MainWindow", "暂停", None))

    def timeoutInturrupt_100ms(self):
        self.currentModeText.setText(self.runningModeMap[self.runningMode])# 设置 当前状况 信息
        #检测当前设备数量有没有变化
        currentComs=set()
        serialLists=list(serial.tools.list_ports.comports())
        comboxCount=0
        if(len(serialLists)!=0):
            for serialInfo in serialLists:
                serialName=serialInfo[0]
                currentComs.add(serialName)
        if(currentComs!=self.currentComs):#设备列表发生变化
            self.currentComs=currentComs
            self.currentComsMap={}
            self.comSelect.clear()
            comboxCount=0
            for serialName in self.currentComs:
                self.currentComsMap[comboxCount]=serialName
                self.comSelect.insertItem(comboxCount,_fromUtf8(serialName))
                comboxCount+=1
            if(len(self.currentComs)==0):
                self.comSelect.insertItem(comboxCount,_fromUtf8(""))

    def modeSelectChange(self):
        self.runningMode=self.modeSelectComboBox.currentIndex()

    def deviceSelectChange(self):
        selectIndex=self.comSelect.currentIndex()
        print "[+]Select index is ",selectIndex
        if(selectIndex in self.currentComsMap):
            self.currentComSelect=self.currentComsMap[selectIndex]
            self.device=serial.Serial(self.currentComSelect,self.deviceBaud)#更改设备串口号
            print "[+]Current com name:",self.currentComSelect

    def frequencyChange(self):
        self.frequency=self.frequencyInputText.text()
        command="<F:{}>".format(self.frequency)
        print "[+]Command:",command
        self.device.write(command)
        print "[+] Written completed!"

    def pulsewidthChange(self):
        self.pulseWidth=self.pulseWidthInputText.text()
        command="<P:{}>".format(self.pulseWidth)
        print "[+]Command:",command
        self.device.write(command)
        print "[+] Written completed!"
    def pwmChange(self):
        self.pwm=self.text_pwm.text()
        command="<W:{}>".format(self.pwm)
        print "[+]Command:",command
        self.device.write(command)
        print "[+] Written completed!"
    def setParameter(self,state):
        if(state==True):
            self.frequency=self.frequencyInputText.text()
            self.pulseWidth=self.pulseWidthInputText.text()
            self.pwm=self.text_pwm.text()
            print "[+]Set",self.currentComSelect,"Params:",
            if(self.runningMode==2):#连续波
                print "ContinousWave"
                command="<C:0><P:{}><F:{}><W:{}>".format(self.pulseWidth,self.frequency,self.pwm)
                print "[+]Command:",command
            elif(self.runningMode==1):#断续波
                print "StopandaheadWave"
                command="<C:2><P:{}><F:{}><W:{}>".format(self.pulseWidth,self.frequency,self.pwm)
                print "[+]Command:",command
            elif(self.runningMode==0):#疏密波
                print "DensityWave"
                command="<C:1><P:{}><F:{}><W:{}>".format(self.pulseWidth,self.frequency,self.pwm)
                print "[+]Command:",command
        else:#停止运行
            command="<X>"
            print "[+]Set",self.currentComSelect," Stop"
            print "[+]Command:",command
        try:
            self.device.write(command)
            print "[+] Written completed!"
        except Exception as e:
            print "[-] Written error,",e

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HelloPyQt = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(HelloPyQt)
    HelloPyQt.show()
sys.exit(app.exec_())
