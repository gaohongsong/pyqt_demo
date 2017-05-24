#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

# create ui by designer and conver to py
from ui import app_ui


# not use ui from qt_designer
def main(argv):
    # print 'start main window.'
    app = QtGui.QApplication(argv)
    widget = QtGui.QWidget()
    widget.resize(200, 150)
    widget.setWindowTitle('hello world')
    widget.show()
    sys.exit(app.exec_())


# use ui from qt_designer way 1
class TestUi_Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = app_ui.Ui_Dialog()
        self.ui.setupUi(self)


# use ui from qt_designer way 2
class TestUi_Dialog1(QtGui.QDialog, app_ui.Ui_Dialog):
    def __init__(self):
        super(TestUi_Dialog1, self).__init__()
        self.setupUi(self)


def ui_main(argv):
    app = QtGui.QApplication(argv)
    # dialog = TestUi_Dialog()
    dialog = TestUi_Dialog1()
    dialog.show()
    app.exec_()


if __name__ == '__main__':
    # main(sys.argv)
    ui_main(sys.argv)
