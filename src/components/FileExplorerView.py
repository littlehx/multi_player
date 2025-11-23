#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :FileExplorerView
# @Time      :2025/11/22 20:56
# @Author    :littlehx
# @Desc      :
import os.path
from pathlib import Path

from PySide6.QtWidgets import QTreeView, QFileSystemModel
from PySide6.QtCore import QDir, Signal

from src.common.log_utils import log_exception, logger
from src.config.settings import Settings
from src.config import env




class FileExplorerView(QTreeView):
    select_dir = Signal(list) # 选择了哪些路径

    def __init__(self, parent=None,
                 root_path:str|Path = Path.home()):
        super().__init__(parent)
        # 启用拖放
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(self.DragDropMode.DropOnly)

        self.file_model = QFileSystemModel(self)
        self.file_model.setRootPath(str(root_path))

        # 设置过滤器,只显示目录
        self.file_model.setFilter(QDir.Filter.NoDotAndDotDot|QDir.Filter.AllDirs)
        self.setModel(self.file_model)
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
        self.header().hide()

        self.selectionModel().selectionChanged.connect(self.on_selection_change)
        Settings()

        # TODO 如果有上一次打开的DIR,就优先打开
        if Settings().get('last_expand_dir'):
            self.open_tree_view(Settings().get('last_expand_dir'))
        else:
            self.open_tree_view(Path.home())

        self.cur_select_path_list = []

    @log_exception
    def on_selection_change(self,*args,**kwargs):
        """
        选中的路径发生更改时触发
        :return:
        """
        indices = self.selectionModel().selectedIndexes()
        paths = [self.file_model.filePath(index) for index  in indices if index.column() == 0]
        # 记录选择的路径列表
        self.cur_select_path_list = paths
        if paths:
            Settings().set('last_expand_dir',paths[0])
        logger.debug(f'select paths:{paths}')
        # 发出信号
        self.select_dir.emit(paths)


    @log_exception
    def open_tree_view(self,path):
        """
        逐级展开所需要的路径
        :param path:
        :return:
        """
        path = os.path.normpath(path.strip())

        # 逐级展开路径
        dir_path = ""
        for folder in path.split(os.sep):
            dir_path = dir_path + os.sep + folder
            if not dir_path.endswith(os.sep):
                dir_path += os.sep
            self.expand(self.model().index(dir_path))

        # 高亮显示最后一个路径
        self.setCurrentIndex(self.model().index(path))








