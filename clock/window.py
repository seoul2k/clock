
from sys import exit, argv
from threading import Thread
from time import sleep, strftime
from datetime import datetime
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QPushButton, QApplication, QHBoxLayout, QSpinBox)
from PyQt5.QtGui import QIcon
from popup import NotificationWindow
import rumps


class clockApp(rumps.App):
    @rumps.clicked("running")
    def prefs(self, _):
        init()


s = True
lt = ['red', 'blue', 'yellow', 'pink', 'green']
i = 0


class App(QWidget):
    def __init__(self,  title, geometry=(300, 300, 200, 200)):
        super().__init__()
        self.initUI(geometry, title)

    def jieshu(self, a, b, c):
        NotificationWindow.info('时间到', '计时时间到：计时{}小时{}分钟{}秒'.format(a, b, c))

    def updataTime(self):
        global i
        while True:
            if i >= len(lt):
                i = i % len(lt)
            self.time.setText(strftime('%Y-%m-%d  %H:%M:%S') +
                              '   星期'+str(datetime.now().isoweekday()))
            i += 1
            sleep(1)

    def times(self, a, b, c):
        y = ((a+b)*60)+c
        for x in range(y):
            self.QL.setText('小时:%s' % (str(x // 60 % 60)))
            self.QL2.setText('分钟:%s' % (str(x // 60)))
            self.QL3.setText('秒:%s' % (str(x % 60)))
            sleep(1)
        self.QL.setText('小时:')
        self.QL2.setText('分钟:')
        self.QL3.setText('秒:')

    def kaishi(self):
        global s
        a = self.Qtext.value()
        b = self.Qtext2.value()
        c = self.Qtext3.value()
        self.QL.setText('开始计时')
        self.button.setHidden(True)
        self.Qtext.setHidden(True)
        self.Qtext3.setHidden(True)
        self.Qtext2.setHidden(True)
        t = Thread(target=self.times, args=(a*60, b, c))
        t.start()
        t.join()
        self.Qtext.setHidden(False)
        self.button.setHidden(False)
        self.Qtext3.setHidden(False)
        self.Qtext2.setHidden(False)
        self.jieshu(a, b, c)

    def initUI(self, geometry, title):
        geom1, geom2, geom3, geom4 = geometry
        self.setGeometry(geom1, geom2, geom3, geom4)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('clock/images/icon.png'))
        self.time = QLabel(self)
        self.time.move(-45, 0)
        self.time.setStyleSheet('color: {};'.format(lt[i]))
        self.QL = QLabel('小时：')
        self.QL.move(10, 20)
        self.Qtext = QSpinBox()
        self.Qtext.setStyleSheet('background: #409eff;')
        self.QL2 = QLabel('分钟：')
        self.QL2.move(10, 20)
        self.Qtext2 = QSpinBox()
        self.Qtext2.setStyleSheet('background: #409eff;')
        self.QL3 = QLabel('秒：')
        self.QL3.move(10, 20)
        self.Qtext3 = QSpinBox()
        self.Qtext3.setStyleSheet('background: #409eff;')
        self.button = QPushButton(QIcon('clock/images/kaishi.png'), '开始')
        self.button.clicked.connect(self.kaishi)
        self.button.setToolTip("index")
        self.layout = QHBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.time)
        self.layout.addLayout(self.layout1)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.QL)
        self.layout.addWidget(self.Qtext)
        self.layout.addWidget(self.QL2)
        self.layout.addWidget(self.Qtext2)
        self.layout.addWidget(self.QL3)
        self.layout.addWidget(self.Qtext3)
        t = Thread(target=self.updataTime)
        t.start()
        self.setLayout(self.layout)
        self.show()


def init():
    app = QApplication(argv)
    ex = App('计时器')
    exit(app.exec_())


if __name__ == "__main__":
    clockApp("clock App").run()
