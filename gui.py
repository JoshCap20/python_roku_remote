from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
import rokuremote as roku
import sys
import app as apppp
import threading
from time import sleep
import time

class Remote(QWidget):
    def __init__(self, parent=None):
        super(Remote, self).__init__(parent)
        #self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint)
        self.setGeometry(10, 40, 140, 30)
        self.initUI()
        self.show()
        


    def launchscript(self):
        apppp.runscript()

    def initUI(self):
        layout = QVBoxLayout()

        # Channels/Inputs
        xbox = QPushButton('Xbox')
        netflix = QPushButton('Netflix')
        hulu = QPushButton('Hulu')
        disneyplus = QPushButton('Disney Plus')
        hbomax = QPushButton('HBO Max')

        # Shows for quick access
        southpark = QPushButton('Southpark')
        modernfamily = QPushButton('Modern Family')
        got = QPushButton('GoT')
        workaholics = QPushButton('Workaholics')

        # Remote features
        home = QPushButton('Home')
        select = QPushButton('Select')
        up = QPushButton('Up')
        down = QPushButton('Down')
        right = QPushButton('Right')
        left = QPushButton('Left')
        #volup = QPushButton('Volume Up')
        #voldown = QPushButton('Volume Down')
        poweroff = QPushButton('Power Off')

        # Other
        music = QPushButton('Music')
        start = QCheckBox('Start')
        self.search = QLineEdit('Search')
        hand_control = QCheckBox('Gestures')
        # Search access
        hulu_search = QPushButton('Hulu Search')
        hbo_search = QPushButton('HBO Search')
        search_button = QPushButton('OK', self)
        pin = QCheckBox('Pin')

        # Volume slider
        sld = QSlider(Qt.Orientation.Horizontal, self)
        sld.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sld.setGeometry(10, 40, 140, 30)
        sld.valueChanged[int].connect(self.changeValue)
        sld.setValue(25)
        sld.setSingleStep(5)
        sld.setTickInterval(5)
        sld.setTickPosition(QSlider.TickPosition.TicksBelow)
        sld.setMinimum(0)
        sld.setMaximum(50)

        # Add each button to layout
        layout.addWidget(start)
        layout.addWidget(pin)
        layout.addWidget(poweroff)
        layout.addWidget(home)
        layout.addWidget(select)
        layout.addWidget(up)
        layout.addWidget(down)
        layout.addWidget(right)
        layout.addWidget(left)
        #layout.addWidget(volup)
        #layout.addWidget(voldown)
        layout.addWidget(xbox)
        layout.addWidget(netflix)
        layout.addWidget(hulu)
        layout.addWidget(disneyplus)
        layout.addWidget(hbomax)
        layout.addWidget(southpark)
        layout.addWidget(modernfamily)
        layout.addWidget(got)
        layout.addWidget(workaholics)
        layout.addWidget(music)
        layout.addWidget(hulu_search)
        layout.addWidget(hbo_search)
        layout.addWidget(hand_control)
        layout.addWidget(self.search)
        layout.addWidget(search_button)
        layout.addWidget(sld)
        
        
    

        # Link buttons to functions in rokutest.py
        xbox.clicked.connect(roku.play_xbox)
        netflix.clicked.connect(roku.watch_netflix)
        hulu.clicked.connect(roku.watch_hulu)
        hbomax.clicked.connect(roku.watch_hbo_max)
        disneyplus.clicked.connect(roku.watch_disney_plus)
        southpark.clicked.connect(roku.southpark)
        got.clicked.connect(roku.game_of_thrones)
        modernfamily.clicked.connect(roku.modernfamily)
        workaholics.clicked.connect(roku.workaholics)
        home.clicked.connect(roku.home)
        select.clicked.connect(roku.select)
        up.clicked.connect(roku.up)
        down.clicked.connect(roku.down)
        right.clicked.connect(roku.right)
        left.clicked.connect(roku.left)
        #volup.clicked.connect(roku.volume_up)
        #voldown.clicked.connect(roku.volume_down)
        poweroff.clicked.connect(roku.power)
        music.clicked.connect(roku.music)
        start.stateChanged.connect(lambda:self.btnstate(start))
        hulu_search.clicked.connect(roku.hulu_search)
        hbo_search.clicked.connect(roku.hbo_max_search)
        search_button.clicked.connect(self.clickMethod)
        pin.clicked.connect(self.togglePin)
        hand_control.stateChanged.connect(lambda:self.gesturesstate(hand_control))

        # Window, Layout Options
        self.setWindowTitle("Remote")
        self.setLayout(layout)

    def clickMethod(self):
        print('Your search: ' + self.search.text())
        for char in self.search.text():
            roku.letter(char)
        self.search.clear()

    def changeValue(self):
        initial_volume: int = 25
        volume_level = self.sender().value()
        if volume_level > initial_volume:
            for i in range(volume_level-initial_volume):
                roku.volume_up()
            initial_volume = volume_level
        if volume_level < initial_volume:
            for i in range(initial_volume-volume_level):
                roku.volume_down()
            initial_volume = volume_level



    def togglePin(self):
        pass
            
    def btnstate(self,start):
        if start.text() == "Start":
            if start.isChecked() == True:
                roku.set_start()
                print("Start selected")
            else:
                roku.set_start_off()
                print("Start deselected")


    def gesturesstate(self,input):
        if input.text() == "Gestures":
            if input.isChecked() == True:
                start_time = time.time()
                print("Gestures selected")
                import os, subprocess
                global p
                p = subprocess.Popen('python /Users/joshuacaponigro/Desktop/hand-gesture-remote/app.py', stdout=subprocess.PIPE, shell=True)
                #self.launchscript()
                if (time.time() - start_time) > 500:
                    self.endscript()
                    p.kill()
            else:
                p.kill()
                print("Gestures deselected")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    remote = Remote()
    remote.show()
    sys.exit(app.exec()) 