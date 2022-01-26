from bottle import route, run, template, request, static_file, debug, response
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='db_emocion')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='files/')

@route('/list')
def list():
    global cnx
    cursor = cnx.cursor()
    query = ("SELECT * FROM crud_employees")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return template('list_template', rows=result)

@route ('/new')
def new():
    return template('new_employee.tpl')

@route('/edit/<no>', method='GET')
def edit(no):
    global cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM crud_employees WHERE id = %s", (no,))
    result = cursor.fetchone()
    cursor.close()
    return template('edit_employee.tpl', row=result, no=no)

@route('/save', method='POST')
def save():
    global cnx

    mode = request.POST.mode.strip()
    id = request.POST.Id.strip()
    names = request.POST.Names.strip()
    address = request.POST.Address.strip()
    date_register = request.POST.Date_register.strip()
    phone = request.POST.Phone.strip()
    comment = request.POST.Comment.strip()
    salary = request.POST.Salary.strip()

    cursor = cnx.cursor()
    if mode == "new":
        cursor.execute( "INSERT INTO crud_employees (names, address, date_register, phone, comment, salary) VALUES (%s, %s, %s, %s, %s, %s)", (names, address, date_register, phone, comment, salary) )
        message =  '<p>El nuevo empleado fue agregado a la base de datos</p><p><a href="/list">Regresar al listado</a></p>'

    if mode == "update":
        cursor.execute( "UPDATE crud_employees SET names=%s, address=%s, date_register=%s, phone=%s, comment=%s, salary=%s WHERE id= %s", (names, address, date_register, phone, comment, salary, id) )
        message = '<p>Datos del empleado actualizados</p><p><a href="/list">Regresar al listado</a></p>'

    cnx.commit()
    cursor.close()
    return message

from mysql.connector import Error
import json

@route('/delete/<no>', method='GET')
def delete(no):
    global cnx
    response.headers['Content-Type'] = 'application/json'
    try:
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM crud_employees WHERE id = %s", (no,))
        cnx.commit()
        results = {'result':'true', 'message':'Eliminacion exitosa'}
        return json.dumps(results)

    except mysql.connector.Error as error:
        results = {'result':'false', 'message':error}
        return json.dumps(results)

    finally:
        if (cnx.is_connected()):
            cursor.close()

debug(True)
run(host='localhost', port=8080)
