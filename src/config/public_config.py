#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :public_config
# @Time      :2025/1/5 20:03
# @Author    :littlehx
# @Desc      :
import os
from os.path import join, dirname, abspath

APP_PATH = dirname(dirname(abspath(__file__)))
DATA_DIR = join(APP_PATH,"data") # 放置生成的数据文件夹路径
os.makedirs(DATA_DIR, exist_ok=True)
LOG_DIR= join(APP_PATH,"logs")
os.makedirs(LOG_DIR, exist_ok=True)