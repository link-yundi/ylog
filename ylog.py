# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2024/6/30 02:37
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""
import inspect
import logging
import os
import sys
import time
import traceback

import colorlog

# ======================== 颜色配置 ========================
logColorsConfig = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

# ======================== 输出格式 ========================
logFormat = {
    "console": "%(log_color)s%(asctime)s %(message)s",
    "file": "%(asctime)s %(message)s"
}

formatter = colorlog.ColoredFormatter(logFormat["console"], log_colors=logColorsConfig)

# #日志名称和日志路径
_LogTime = time.strftime('%Y%m%d', time.localtime(time.time()))
_log_path = os.path.join('', 'logs')
if os.path.isdir(_log_path):
    pass
else:
    os.mkdir(_log_path)
logfile = os.path.join(_log_path, f'{_LogTime}.log')

LEVEL_DEBUG = logging.DEBUG
LEVEL_INFO = logging.INFO
LEVEL_WARNING = logging.WARNING
LEVEL_ERROR = logging.ERROR


# ##############################   logging 基础设置   ################################
def _init_ylog(level=LEVEL_INFO):
    root_logger = logging.getLogger()

    if not root_logger.handlers:
        logging.basicConfig(level=level,
                            format=logFormat["file"],
                            datefmt="%Y-%m-%d %H:%M:%S",
                            filename=logfile,
                            filemode='a')

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler(stream=sys.stdout)
        console.setLevel(level)  # DEBUG INFO WARNING ERROR
        formatter.datefmt = "%Y-%m-%d %H:%M:%S"
        console.setFormatter(formatter)
        # 获取根目录记录器并添加处理器
        root_logger.setLevel(level)
        root_logger.addHandler(console)
    else:
        root_logger.setLevel(level)
    return logging


_logger = _init_ylog()


def set_level(level):
    global _logger
    _logger = _init_ylog(level)


def _msg_(prefix, *msg) -> str:
    frame = inspect.stack()[2]
    M = f'[{prefix.upper()}] File "{frame.filename}", line {max(frame.lineno, 1)}: '.replace("\\", "/")
    for m in msg:
        M += f"{m} "
    return M


def Info(*msg):
    _logger.info(_msg_("info", *msg))


def Warn(*msg):
    _logger.warning(_msg_("warning", *msg))


def Debug(*msg):
    _logger.debug(_msg_("debug", *msg))


def Error(*msg):
    _logger.error(f'{_msg_("error", *msg)} \n {traceback.format_exc()}')

