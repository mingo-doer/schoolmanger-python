#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "cc"
# Date: 2018/11/8


class Classes:
    def __init__(self,school,name,course,student_path):
        self.shool = school
        self.name = name  # 班级名称
        self.course = course  # 班级科目
        self.student_path = student_path    # 学生信息文件路径

class Course:
    def __init__(self,name,period,price,school):
        self.name = name
        self.period = period    # 课程周期
        self.price = price
        self.school = school    # 课程所属学校

    def __repr__(self):
        return self.name

class School:
    def __init__(self,name,course):
        self.name = name
        self.course = course

if __name__ == '__main__':
    from 校园管理系统.conf.config import schoolinfo
    from 校园管理系统.core.my_pickle import MyPickle
    school_pickle = MyPickle(schoolinfo)
    python = Course('python','6 month',19800,'北京校区')
    linux = Course('linux','5 month',12800,'北京校区')
    go = Course('go','4 month',12800,'上海校区')
    beijing = School('北京校区',[linux,python])
    shanghai = School('上海校区',[go])
    school_pickle.dump(beijing)
    school_pickle.dump(shanghai)















