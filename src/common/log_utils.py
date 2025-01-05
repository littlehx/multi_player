#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :log_utils
# @Time      :2025/1/5 19:59
# @Author    :littlehx
# @Desc      :
import logging
import os
import traceback
from curses import wrapper
from datetime import datetime
from functools import wraps

from config.public_config import LOG_DIR


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
log_path = os.path.join(LOG_DIR,datetime.now().strftime('日志_%Y_%m_%d') + '.log')
logger = setup_logger(log_path)

def log_exception(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 记录错误堆栈信息到日志
            error_message = f"Exception in function '{func.__name__}': {str(e)}"
            error_stack = traceback.format_exc()
            logger.error(f"{error_message}\n{error_stack}")
            # 继续抛出异常，以便调用者可处理
            raise e
    return inner
