#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "cc"
# Date: 2018/11/7
import os
import pickle

from core.school import Course
from core.school import Classes
from core.teacher import *


class MyPickle:
    def __init__(self,filename):
        self.filename = filename

    def dump(self,obj):
        with open(self.filename,'ab',encoding='utf-8') as f:
            pickle.dump(obj,f)

    def loaditer(self):
        with open(self.filename,'rb',encoding='utf-8') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except: break

    def edit(self,obj):   # 修改
        f2 = MyPickle(self.filename+'.bak')
        for item in self.loaditer():
            if item.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(item)
        os.remove(self.filename)
        os.rename(self.filename+'.bak',self.filename)



