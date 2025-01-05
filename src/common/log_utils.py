#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :log_utils
# @Time      :2025/1/5 19:59
# @Author    :littlehx
# @Desc      :
import logging
from datetime import datetime


def setup_logger(log_file):
    # 创建一个日志记录器对象
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # 创建一个用于写入日志文件的处理器
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # 创建一个用于标准输出流的处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 创建日志格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 将格式器添加到处理器
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# 使用示例
log_file = datetime.now().strftime('日志_%Y_%m_%d') + '.log'
logger = setup_logger(log_file)

logger.info('This is an info message.')
logger.error('This is an error message.')
