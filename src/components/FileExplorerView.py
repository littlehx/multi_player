#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :FileExplorerView
# @Time      :2025/11/22 20:56
# @Author    :littlehx
# @Desc      :
from pathlib import Path

from PySide6.QtWidgets import QTreeView
class FileExplorerView(QTreeView):
    def __init__(self, parent=None,root_path = Path.home()):
        super().__init__(parent)