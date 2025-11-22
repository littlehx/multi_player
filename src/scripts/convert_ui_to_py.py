#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :convert_ui_to_py
# @Time      :2025/11/22 20:11
# @Author    :littlehx
# @Desc      :
import os.path
import subprocess

import logging
logger = logging.getLogger(__name__)
# from src.common.log_utils import logger
from src.config.public_config import BASE_DIR, SRC_DIR
import src.common.log_utils

if __name__ == '__main__':
    ui_dir = BASE_DIR / 'src' / 'resources' / 'ui'
    for ui_file in ui_dir.rglob('*.ui'):
        base_name = ui_file.stem
        py_file = list(SRC_DIR.rglob(base_name + '.py'))
        assert len(py_file) <= 1,f"寻找到多个同名的{ui_file}对应的py文件"
        if len(py_file) == 0:
            py_file_path = ui_dir / (base_name + '.py')
        else:
            py_file_path = py_file[0]

        cli = [
            'pyside6-uic',
            str(ui_file),
            '-o', str(py_file_path),
        ]
        process = subprocess.Popen(cli, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = process.communicate(timeout=10)
        logger.debug(f"out:{out},err:{err}")
    logger.debug(f"ui文件转化完成")

