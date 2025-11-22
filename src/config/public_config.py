#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :public_config
# @Time      :2025/1/5 20:03
# @Author    :littlehx
# @Desc      :
import os
from os.path import join, dirname, abspath
from pathlib import Path

BASE_DIR = Path(dirname(dirname(abspath(__file__)))).parent # 项目入口文件夹)
DATA_DIR = join(BASE_DIR, "data") # 放置生成的数据文件夹路径
SRC_DIR = BASE_DIR / 'src'
os.makedirs(DATA_DIR, exist_ok=True)
LOG_DIR= join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)