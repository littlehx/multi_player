#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :log_utils
# @Time      :2025/1/5 19:59
# @Author    :littlehx
# @Desc      :
import logging
import os
import time
import traceback
from functools import wraps
from logging.handlers import TimedRotatingFileHandler

from src.config import env



def setup_global_logging(log_file):
    # 移除所有已存在的处理器（避免重复日志）
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.root.setLevel(logging.DEBUG)

    # 定时切割处理器——每天生成一个新文件，保留30天的日志
    file_handler = TimedRotatingFileHandler(
        log_file,
        when='midnight',       # 每天午夜切分
        interval=1,            # 间隔一天
        backupCount=30,        # 最多保留30个文件
        encoding='utf-8',      # 推荐加上编码
        utc=False              # 使用本地时间
    )
    file_handler.setLevel(logging.DEBUG)

    # 文件处理器
    # file_handler = logging.FileHandler(log_file)
    # file_handler.setLevel(logging.DEBUG)
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # 格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加到 root logger
    logging.root.addHandler(file_handler)
    logging.root.addHandler(console_handler)


log_path = os.path.join(env.LOG_DIR, 'main.log')

# 一般在入口处调用一次
setup_global_logging(log_path)


def setup_logger(log_file):
    # 创建一个日志记录器对象
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # # 创建一个用于写入日志文件的处理器
    # file_handler = logging.FileHandler(log_file)
    # file_handler.setLevel(logging.DEBUG)
    #
    # # 创建一个用于标准输出流的处理器
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)
    #
    # # 创建日志格式器
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #
    # # 将格式器添加到处理器
    # file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)
    #
    # # 将处理器添加到记录器
    # logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logger

# 使用示例
logger = setup_logger(log_path)

def log_exception(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            start = time.time()
            ret =  func(*args, **kwargs)
            end = time.time()
            logger.debug(f"func {func.__name__} takes {end - start} seconds")
            return ret
        except Exception as e:
            # 记录错误堆栈信息到日志
            error_message = f"Exception in function '{func.__name__}': {str(e)}"
            error_stack = traceback.format_exc()
            logger.error(f"{error_message}\n{error_stack}")
            # 继续抛出异常，以便调用者可处理
            raise e
    return inner
