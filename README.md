# schoolmanger-python
校园管理系统 python3.6
操作管理(OperationManagement)


使用面向对象创建多所学校
在学校内创建多所课程，比如AI, Python , ML 3个课程 ，AI\Python 在上海开， ML 在纽约开
课程包含，周期，价格
通过学校创建课程
创建学员时，选择关联学校，选择关联课程
创建讲师角色时要关联学校， 在完成功能的同时要保证数据的之间的关联关系
提供三个角色接口
学员视图：可以注册，登陆，选择学校，选择课程，查看分数，退出登录
讲师视图：可以登陆，选择课程，查看课程，查看学生，修改分数，退出登录
管理视图：可以注册，登陆，创建学校，创建课程，创建老师，退出登录
上面的操作产生的数据都通过pickle序列化保存到文件里


要求：

使用软件开发规范做分层式架构设计：至少包含用户输入层，数据接口层和数据处理层，尽力避免代码冗余，公用的功能可放置于 /lib-common.py 下面。

