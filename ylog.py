# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2024/6/30 02:37
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""
import os
import time
import traceback

from loguru import logger

# #日志名称和日志路径
_LogTime = time.strftime('%Y%m%d', time.localtime(time.time()))
_log_path = os.path.join('', 'logs')
if os.path.isdir(_log_path):
    pass
else:
    os.mkdir(_log_path)
logfile = os.path.join(_log_path, f'{_LogTime}.log')

logger.add(logfile)

add = logger.add


def info(*msg):
    logger.opt(depth=1).info(" ".join([str(m) for m in msg]))


def warning(*msg):
    logger.opt(depth=1).warning(" ".join([str(m) for m in msg]))


def error(*msg):
    err_msg = " ".join([str(m) for m in msg])
    err_msg = f"""
=========================================================================
[error message]
{err_msg}
=========================================================================
[traceback]
{traceback.format_exc()}
=========================================================================
"""
    logger.opt(depth=1).error(err_msg)


def debug(*msg):
    logger.opt(depth=1).debug(" ".join([str(m) for m in msg]))
