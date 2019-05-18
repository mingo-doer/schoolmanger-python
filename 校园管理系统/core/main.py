#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "cc"
# Date: 2018/11/3


import sys
from 校园管理系统.conf.config import *
from 校园管理系统.core.manager import Manager        # 反射的时候用

def login():
    '''
    登入韩式，应该先到conf.config文件中读取userinfode的文件路径
    读取userinfo文件中的信息，对应户名和密码进行检查
    登入成功后，查看这个人的额身份，来确定进入哪个图示
    :return:
    '''
    usr = input('username: ')
    pwd = input('password: ')
    with open(userinfo,encoding='utf-8') as f:
        for line in f :
            usrname,passwd,role = line.strip().split('|')
            if usrname == usr and passwd == pwd:
                print('\033[1;32m登入成功！\033[0m')
                return {'username':usr,'role':role}
            else:
                print('\033[1;31m登入失败!\033[0m')

def main():
    '''
    打印欢迎信息
    login：得到返回值：用户姓名和身份
    打印用户身份对应的功能菜单
    如何用户要调用任何方法应该通过角色对象调用，跳转到对应对象的方法里
    :return:
    '''
    # sys.modules是一个字典，内部包含模块名与模块对象的映射，该字典决定了导入模块时是否需要重新导入。
    print('\033[1;42m欢迎登入选课系统\033[0m')
    ret = login()     # ret现在是字典
    if ret:
        role_class = getattr(sys.modules[__name__],ret['role'])      # 反射对应的角色类
        '''
        sys.modules是导入新的模块，sys.modules都将记录这些模块。是字典
        1. 如果模块是被导入，__name__的值为模块名字
        2. 如果模块是被直接执行，__name__的值为’__main__’
        综上：sys.modules[__name__]  的意思就是当前页面的所有模块
        '''
        obj = role_class(ret['username'])
        while True:
            for i,j in enumerate(role_class.menu,1):
                print(i,j[0])
            # try:
            ret = int(input('请输入序号：'))
            getattr(obj,role_class.menu[ret-1][1])()    # 反射
            # except:
            #     print('对不起。您输入的内容有误！')
