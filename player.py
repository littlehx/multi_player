#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :player.py
# @Time      :2025/1/5 15:19
# @Author    :littlehx
# @Desc 入口文件
import sys

from PySide6.QtWidgets import QApplication

from src.view.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())