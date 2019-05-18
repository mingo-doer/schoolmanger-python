#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "cc"
# Date: 2018/11/3

# 管理员

from os import path
from 校园管理系统.conf.config import *
from 校园管理系统.core.school import *
from 校园管理系统.core.teacher import Teacher
from 校园管理系统.core.student import Student
from 校园管理系统.core.my_pickle import MyPickle


class Manager:
    menu = [('创建讲师账号','createTeacher'),('创建学生账号','createStudent'),
            ('查看学校','showSchool'),('查看讲师','showTeacher'),
            ('查看课程','showCourse'),
            ('创建班级','createClasses'),('查看班级','showClasses'),
            ('为班级指定老师','boundClassTeacher'),('退出','exit')]

    def __init__(self,name):
        self.name = name
        self.teacher_pickle_obj = MyPickle(teacher_obj)    # mypickle的对象
        self.course_pickle_obj = MyPickle(course_obj)
        self.school_pickle_obj = MyPickle(schoolinfo)
        self.class_pickle_obj = MyPickle(classes_obj)

    @staticmethod
    def userinfo_handle(content):       # 信息存入userinfo
        with open(userinfo,'a',encoding='utf-8') as f:
            f.write('\n%s'%content)

    def createTeacher(self):
        '''
        输入讲师姓名，输入讲师密码，将讲师信息写入userinfo文件
        输入讲师所在学校
        实例化一个讲师对象（用户名、身份、学校），储存在讲师对应的文件中
        :return:
        '''
        teacher_name = input('请输入要创建的讲师姓名：')
        teacher_passwd = input('请输入要创建的讲师密码：')
        self.showSchool()
        school = input('学校：')
        content = '%s|%s|Teacher'%(teacher_name,teacher_passwd)
        Manager.userinfo_handle(content)
        teacher = Teacher(teacher_name,school)    # 实例化
        self.teacher_pickle_obj.dump(teacher)
        print('创建成功')

    def show(self,pickle_obj):
        pick_obj = getattr(self,pickle_obj)    # 就可以拿到对应属性的mypickle的对象（如teacher_pickle_obj）
        load_g = pick_obj.loaditer()           # 返回的生成器
        for course_obj in load_g:
            for i in course_obj.__dict__:
                print(i,course_obj.__dict__[i])
            print('-' * 50)

    def showCourse(self):
        self.show('course_pickle_obj')

    def showSchool(self):
        self.show('school_pickle_obj')

    def showClasses(self):
        self.show('class_pickle_obj')

    def showTeacher(self):
        self.show('teacher_pickle_obj')


    def createClasses(self):
        '''
        输入：班级名称、学校
        绑定学科对象，要先调用查看学科方法获取学科对象，用户选择学科，再将对象绑定到班级
        创建一个属于这个班级的文件用于储存学生信息，将文件路径储存到班级对象中
        创建一个班级对象（名称、学校、学科对象、讲师空列表、学生信息储存路径）存入classes
        :return:
        '''
        class_name = input('请输入班级的名称：')
        self.showSchool()
        school_name = input('请输入学校的名称：')
        self.showCourse()
        course = input('请输入学科的名称：')
        student_path = path.join(studentinfo,class_name)      # 路径拼接（studentinfo是路径 + class_name）
        open(student_path,'w',encoding='utf-8').close()    # 在文件夹中创建空文档
        class_obj = Classes(school_name,class_name,course,student_path)
        self.class_pickle_obj.dump(class_obj)


    def createStudent(self):
        '''
        输入：学生姓名、密码，写入userinfo文件中
        创建学生对象（姓名，讲师空列表）
        :return:
        '''
        student_name = input('请输入学生姓名：')
        student_pwd = input('请输入学生密码：')
        self.showSchool()
        student_school = input('请输入学生所有的学校：')
        self.showClasses()
        student_class = input('请输入学生所有的班级：')
        class_g = self.class_pickle_obj.loaditer()   # 读出所有班级信息的生成器
        for clas in class_g:
            if clas.name == student_class:
                content = '%s|%s|Student'%(student_name,student_pwd)
                Manager.userinfo_handle(content)
                stu_obj = Student(student_name,student_school,clas)
                MyPickle(clas.student_path).dump(stu_obj)   # 储存
                print('创建成功！')
                break
        else:
            print('您的输入有误，创建学生失败')

    def boundClassTeacher(self):
        '''
        用show方法找到指定的老师和对应的班级
        给讲师对象的班级属性列表中加入一个新的项，为班级对象
        给班级对象的讲师属性列表中加入一个新的项，为讲师对象
        '''
        self.showClasses()
        class_name = input('输入要指定的班级：')
        self.showTeacher()
        teacher_name = input('输入要指定的老师:')
        teach_g = self.teacher_pickle_obj.loaditer()
        for teacher_obj in teach_g:
            if teacher_obj.name == teacher_name:
                teacher_obj.classes.append(class_name)
                self.teacher_pickle_obj.edit(teacher_obj)
                print('创建成功！')
                return














