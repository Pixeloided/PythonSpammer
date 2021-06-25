from time import sleep
import keyboard
import random
import string
import threading
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect, QStackedWidget
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QPoint, QEasingCurve

class welcomeScreen(QDialog):
    def __init__(self):
        super(welcomeScreen, self).__init__()
        loadUi("resources/welcome.ui", self)
        self.uiScriptBasedSpammer.clicked.connect(self.gotoscript)
        self.uiUniqueSpammer.clicked.connect(self.gotounique)
        self.aboutButton.clicked.connect(self.gotoabout)
        
        self.animation = QPropertyAnimation(self.welcomeLabel, b"pos")
        self.animation.setDuration(1400)
        self.animation.setEndValue(QPoint(50, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        
        self.solaranim = QPropertyAnimation(self.solarLabel, b"pos")
        self.solaranim.setDuration(1400)
        self.solaranim.setEndValue(QPoint(50, 30))
        self.solaranim.setEasingCurve(QEasingCurve.OutCubic)
        
        self.animgroup = QSequentialAnimationGroup()
        self.animgroup.addAnimation(self.animation)
        self.animgroup.addAnimation(self.solaranim)
        self.animgroup.start()
        
    def gotoscript(self):
        scriptBasedScreen = scripted()
        widget.addWidget(scriptBasedScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Script spammer")
        
    def gotounique(self):
        unique = uniqueSpammer()
        widget.addWidget(unique)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Unique spammer")
        
    def gotoabout(self):
        abt = aboutUs()
        widget.addWidget(abt)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - About")

        
class scripted(QDialog):
    def __init__(self):
        super(scripted, self).__init__()
        loadUi("resources/scriptBased.ui", self)
        self.backButton.clicked.connect(self.gotowelcome)
        self.scriptFile.clicked.connect(self.getFile)
        self.startButton.clicked.connect(self.runThread)
        
        self.timeBetweenMessages.setProperty("singleStep", 0.1)
        self.timeBetweenMessages.setProperty("value", 0.4)
        self.timeBetweenMessages.setProperty("decimals", 1)
            
        self.animation = QPropertyAnimation(self.scriptbasedLabel, b"pos")
        self.animation.setDuration(2000)
        self.animation.setEndValue(QPoint(0, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
        
    def gotowelcome(self):
        welcome = welcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Welcome")
              
    def getFile(self):
        self.getFileDialog = QtWidgets.QFileDialog.getOpenFileName()
        try:
            filePathPre = str(self.getFileDialog).split("'")[1]
            if filePathPre == "":
                print("No file selected")
            else:
                global filePath
                filePath = filePathPre
                print(filePath)
                self.scriptFile.setText("Selected")
        except: return
        
    def runThread(self):
        threading.Thread(target=self.run).start()
        
    def run(self):
        try:
            if filePath != "":
                
                self.startButton.setText("Starting in 5 seconds")
                
                file = open(filePath, "r")
                ac = str(file.read())
                
                split_up_script = []
                split_up_script = ac.splitlines()
                splsc = split_up_script
                
                wait_time = self.timeBetweenMessages.value()
                chunkyBoiCount = self.messageBlockSize.value()
                randomTime = self.randomizeTime.checkState()
                
                n_elem = len(split_up_script)
                time_remaining = n_elem * wait_time + n_elem//chunkyBoiCount * wait_time * 1.5
                old_time = time_remaining
                
                
                self.startButton.setText("Starting in 5 seconds.....")
                sleep(1)
                self.startButton.setText("Starting in 4 seconds....")
                sleep(1)
                self.startButton.setText("Starting in 3 seconds...")
                sleep(1)
                self.startButton.setText("Starting in 2 seconds..")
                sleep(1)
                self.startButton.setText("Starting in 1 second.")
                sleep(1)
                
                i = 0
                ln = 0
                self.startButton.setText("Running!")
                
                for split_up_script in split_up_script:
                    if randomTime >= 1:
                        wait_time = round(random.uniform(0.5, 2), 2)
                        self.minutesRemainingLabel.setText("Cannot calculate")
                        
                    ln += 1
                    
                    keyboard.write(splsc[i])
                    sleep(0.001)
                    keyboard.press_and_release("shift+enter")
                    
                    i += 1
                    
                    time_remaining = n_elem * wait_time - i * wait_time + n_elem//chunkyBoiCount * wait_time*1.5
                    time_remaining_minutes = int(time_remaining)//60
                    time_percent = round(time_remaining/old_time * 100)
                    
                    if randomTime == 0:
                        self.minutesRemainingDisplay.setProperty("value", time_remaining_minutes)
                        self.progressBar.setProperty("value", time_percent)
                        
                    print(f"{i}/{n_elem}")
                    
                    if chunkyBoiCount == ln:
                        print("----------")
                        keyboard.press_and_release("enter")
                        ln = 0
                        sleep(wait_time*1.5)
                        
                    sleep(wait_time)
                    
                    if i == n_elem:
                        self.minutesRemainingLabel.setText("Approximate minutes remaining")
                        
        except:
            self.startButton.setText("Please select a script file!")
            sleep(1.5)
            self.startButton.setText("Start!")
        self.startButton.setText("Start!")
        self.progressBar.setProperty("value", 0)
        
class uniqueSpammer(QDialog):
    def __init__(self):
        super(uniqueSpammer, self).__init__()
        loadUi("resources/unique.ui", self)
        self.uniqueBack.clicked.connect(self.gotwelcome)
        self.startButton.clicked.connect(self.runThread)
        
        self.timeBetween.setProperty("singleStep", 0.1)
        self.timeBetween.setProperty("decimals", 1)
        self.timeBetween.setProperty("minimum", 0.1)
        self.timeBetween.setProperty("value", 1.0)
        
        self.suffixLength.setMinimum(4)
        self.suffixLength.setMaximum(100)
        self.suffixLength.setValue(16)
        
        self.spamTimes.setMaximum(7000)
        self.spamTimes.setSingleStep(10)
        self.spamTimes.setProperty("value", 100)
        
        self.animation = QPropertyAnimation(self.uniqueLabel, b"pos")
        self.animation.setDuration(2000)
        self.animation.setEndValue(QPoint(0, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()
        
    def gotwelcome(self):
        welcome = welcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Welcome")
      
    def runThread(self):
        threading.Thread(target=self.run).start()
      
    def run(self):
        
        
        content = self.startingString.text()
        times = self.spamTimes.value()
        waitTime = self.timeBetween.value()
        randomTime = self.randomizeTime.checkState()
        
        STR_GEN = string.ascii_uppercase + string.digits + string.punctuation
        
        d = 0
        
        timeLeftPre = times * waitTime - d * waitTime
        
        self.startButton.setText("Starting in 5 seconds.....")
        sleep(1)
        self.startButton.setText("Starting in 4 seconds....")
        sleep(1)
        self.startButton.setText("Starting in 3 seconds...")
        sleep(1)
        self.startButton.setText("Starting in 2 seconds..")
        sleep(1)
        self.startButton.setText("Starting in 1 second.")
        sleep(1)
        
        self.startButton.setText("Running!")
        
        for i in range(times):
            keyboard.write(content + "  {" + ''.join(random.choice(STR_GEN) for _ in range(self.suffixLength.value())) + "}")
            sleep(0.001)
            keyboard.press_and_release("enter")
            if randomTime == 0:
                sleep(waitTime)
            else:
                sleepyTime = round(random.uniform(0.5, 2), 2)
                sleep(sleepyTime)
            d += 1
            print(f"{d}/{times}")
            timeLeft = times * waitTime - d * waitTime
            self.minutesRemainingDisplay.setProperty("value", round(timeLeft/60))
            self.progressBar.setProperty("value", round(timeLeft/timeLeftPre*100))
            
        self.startButton.setText("Start!")
        
class aboutUs(QDialog):
    def __init__(self):
        super(aboutUs, self).__init__()
        loadUi("resources/about.ui", self)
        self.abtBack.clicked.connect(self.gootowelcome)
        
        self.animation = QPropertyAnimation(self.aboutLabel, b"pos")
        self.animation.setDuration(1400)
        self.animation.setEndValue(QPoint(-10, 30))
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        
        self.solaranim = QPropertyAnimation(self.solarLabel, b"pos")
        self.solaranim.setDuration(1400)
        self.solaranim.setEndValue(QPoint(20, 30))
        self.solaranim.setEasingCurve(QEasingCurve.OutCubic)
        
        self.body = QPropertyAnimation(self.about, b"pos")
        self.body.setDuration(2500)
        self.body.setEndValue(QPoint(200, 150))
        self.body.setEasingCurve(QEasingCurve.OutCirc)
        
        self.animgroup = QSequentialAnimationGroup()
        self.animgroup.addAnimation(self.animation)
        self.animgroup.addAnimation(self.solaranim)
        self.animgroup.addAnimation(self.body)
        self.animgroup.start()
        
    def gootowelcome(self):
        welcome = welcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("{solar} - Welcome")

     
import sys
from ctypes import windll
myappid = 'trident.solar.solar.1.0.0'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
app = QApplication(sys.argv)
welcome = welcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1151)
widget.setFixedHeight(650)
widget.setWindowTitle("{solar} - Welcome")
widget.setWindowIcon(QIcon("assets/icon.png"))
widget.show()
try: sys.exit(app.exec_())
except: pass