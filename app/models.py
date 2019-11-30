from app import db

'''
作业：
    1、实现员工列表页面+添加员工+更新员工+删除员工（头像不加） 新建HTML
    2、分页显示
    3、新建项目，在app.py 中写所有的逻辑函数，然后在models.py 中写model类
'''

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    age = db.Column(db.SmallInteger)
    salary = db.Column(db.Numeric(7,2))