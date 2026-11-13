#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from PyQt4 import QtCore, QtGui, uic  # подключает основные модули PyQt
 
 
# прототип главной формы
class MainForm(QtGui.QDialog):
 
    # конструктор
    def __init__(self):
        super(MainForm, self).__init__()
 
        # динамически загружает визуальное представление формы
        uic.loadUi("mainform.ui", self)
 
        # связывает событие нажатия на кнопку с методом
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"),
            self.setLabelText)
 
    def setLabelText(self):
        self.label.setText("New label text")

