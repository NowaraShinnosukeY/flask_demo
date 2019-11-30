from flask import render_template, Blueprint, request, redirect, url_for
from app import db
from app.models import Employee
emp_blue = Blueprint('emp',__name__,url_prefix='/emp')
@emp_blue.route('/home/')
def emplist():
    if request.args.get('number'):
        number = request.args.get('number')
        emps = db.session.query(Employee).paginate(page=int(number), per_page=3)
    else:
        emps = db.session.query(Employee).paginate(page=1,per_page=3)
    return render_template('emplist.html',emps=emps.items,empspage = emps)

@emp_blue.route('/add/')
def add():
    return render_template('addemp.html')

@emp_blue.route('/addlogic/',methods=['get','post'])
def addEmp():
    name = request.form.get('name')
    age = request.form.get('age')
    salary = request.form.get('salary')
    emp = Employee(name=name,age=age,salary=salary)
    db.session.add(emp)
    db.session.commit()
    return redirect(url_for('emplist'))

@emp_blue.route('/dellogic/')
def delEmp():
    id = request.args.get('id')
    emp = Employee.query.get(int(id))
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('emp.emplist'))

@emp_blue.route('/update/')
def updateEmp():
    id = request.args.get('id')
    name = request.args.get('name')
    age = request.args.get('age')
    salary = request.args.get('salary')
    return render_template('updateemp.html',id=id,name=name,age=age,salary=salary)

@emp_blue.route('/updatelogic/',methods=['get','post'])
def update():
    id = request.form.get('id')
    name = request.form.get('name')
    age = request.form.get('age')
    salary = request.form.get('salary')
    if (name and age and salary):
        emp = Employee.query.get(int(id))
        emp.name = name
        emp.age = age
        emp.salary = salary
        db.session.commit()
        return redirect(url_for('emp.emplist'))
    return render_template('error.html')