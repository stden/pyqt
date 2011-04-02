#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *  # компоненты интерфейса

print "Это отладочный вывод в консоль!"
 
# Каждое приложение должно создать объект QApplication
# sys.argv - список аргументов командной строки
a = QApplication(sys.argv)
 
# QWidget - базовый класс для всех объектов интерфейса
# пользователя; если использовать для виджета конструктор
# без родителя, такой виджет станет окном
w = QWidget()
 
w.resize(320, 240)  # изменить размеры виджета
w.setWindowTitle("Моё первое окно на PyQt!")  # установить заголовок
w.show()  # отобразить окно на экране
 
sys.exit(a.exec_())  # запуск основного цикла приложения

