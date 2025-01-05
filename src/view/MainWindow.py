#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :MainWindow.py
# @Time      :2025/1/5 15:20
# @Author    :littlehx
from PySide6.QtWidgets import QMainWindow

from src.view.main_window import Ui_MainWindow


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
