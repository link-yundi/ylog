# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2025/4/28 13:22
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""

VERSION = '1.0.0'
from setuptools import setup, find_packages

setup(
    name='ylog',
    version=VERSION,
    py_modules=['ylog'],
    install_requires=['colorlog'],

    author='ZhangYundi',
    author_email='yundi.xxii@outlook.com',
    packages=find_packages(include=['ylog', 'ylog.*']),
    description='Logger with colors and traces',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/link-yundi/ylog',

    scripts=[],
    package_data={},
)