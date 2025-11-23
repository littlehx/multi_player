#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :public_config
# @Time      :2025/1/5 20:03
# @Author    :littlehx
# @Desc      :
import os
import platform
import sys
from os.path import join, dirname, abspath
from pathlib import Path

BASE_DIR = Path(dirname(dirname(abspath(__file__)))).parent  # 项目入口文件夹)
DATA_DIR = join(BASE_DIR, "data")  # 放置生成的数据文件夹路径
SRC_DIR = BASE_DIR / 'src'
RESOURCES_DIR = SRC_DIR / 'resources'
os.makedirs(DATA_DIR, exist_ok=True)
LOG_DIR = join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
SETTINGS_DIR = RESOURCES_DIR / "settings"

IS_LINUX = platform.system() == "Linux"
IS_MACOS = platform.system() == "Darwin"
IS_WINDOWS = platform.system() == "Windows"

IS_PYINSTALLER = getattr(sys, "frozen", False)
IS_SNAP = IS_LINUX and "SNAP" in os.environ
IS_APPIMAGE = IS_LINUX and "APPIMAGE" in os.environ
IS_FLATPAK = IS_LINUX and "FLATPAK_ID" in os.environ

PYINSTALLER_LIB_ROOT = (
    Path(sys._MEIPASS) if IS_PYINSTALLER else Path.cwd()  # noqa: WPS437
)

VLC_VERSION = None
VLC_PYTHON_VERSION = None

if IS_FLATPAK:
    FLATPAK_RUNTIME_DIR = (
            Path(os.environ["XDG_RUNTIME_DIR"])
            / "app"
            / os.environ["FLATPAK_ID"]
            / "gridplayer"
    )
    FLATPAK_RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
else:
    FLATPAK_RUNTIME_DIR = None
