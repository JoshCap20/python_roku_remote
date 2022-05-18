from PyQt6.QtWidgets import *
import rokutest as roku
import sys



class Remote(QDialog):
    def __init__(self, parent=None):
        super(Remote, self).__init__(parent)
        self.initUI()
        self.show()

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
        volup = QPushButton('Volume Up')
        voldown = QPushButton('Volume Down')
        poweroff = QPushButton('Power Off')

        # Other
        music = QPushButton('Music')

        # Add each button to layout
        layout.addWidget(poweroff)
        layout.addWidget(home)
        layout.addWidget(select)
        layout.addWidget(up)
        layout.addWidget(down)
        layout.addWidget(right)
        layout.addWidget(left)
        layout.addWidget(volup)
        layout.addWidget(voldown)
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
        volup.clicked.connect(roku.volume_up)
        voldown.clicked.connect(roku.volume_down)
        poweroff.clicked.connect(roku.power)

        # Window, Layout Options
        self.setWindowTitle("Remote")
        self.setLayout(layout)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    remote = Remote()
    remote.show()
    sys.exit(app.exec()) 