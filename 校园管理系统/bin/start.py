#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "cc"
# Date: 2018/11/3

from os import getcwd,path
from sys import path as sys_path
sys_path.insert(1,path.dirname(getcwd()))
# 修改sys.path  把校园管理系统这个路径写到sys.path中
# 之后所有模块导入，都是基于校园管理系统

from core import main
from core.school import *
if __name__ == '__main__':
    main.main()

