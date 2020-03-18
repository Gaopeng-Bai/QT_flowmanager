#!/home/{username}/anaconda3 python
# encoding: utf-8
"""
@author: gaopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: gaopengbai0121@gmail.com
@software: garner
@file: Main.py
@time: 3/18/20 12:59 PM
@desc:
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI.flowmanager import Ui_MainWindow


class GUI_main(Ui_MainWindow):
    def __init__(self, mainwindow):
        super.
        print(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # initialize application
    MainWindow = QMainWindow()  # Create main window
    ui = GUI_main(MainWindow)  # Create UI window
    ui.setupUi(MainWindow)  # 初始化UI到主窗口，主要是建立代码与ui之间的signal与slot
    MainWindow.show()  # present window
    sys.exit(app.exec_())  # It returns 0 after the message loop ends, and then calls sys.exit (0) to exit the program
