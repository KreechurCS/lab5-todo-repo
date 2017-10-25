from flask import Flask, request
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__, static_url_path='')
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todo'
app.config['MYSQL_HOST'] = '104.199.107.34'
mysql.init_app(app)
# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    return str( "List of commands: list/add/delete/update")      #Return the data in a string format

@app.route("/list/")
def list():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM tasks''')
	rv = cur.fetchall()
	ret = "Results: <BR/>"
	for row in rv :
		ret = ret +'(' + row[0] + ',' + row[1] + ')<BR/>'
	return ret

@app.route("/add/<username>/<email>")
def add(username , email) :
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO tasks (taskName, taskDesc) values ('%s','%s')''' % (username, email)) 
	cur.execute('commit;')
	return 'added :)'

@app.route("/update/<name1>/<name2>")
def update(name1, name2) :
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE tasks SET taskName = '%s'  WHERE taskName LIKE '%s' ''' % (name1 , name2))
        cur.execute('commit;')
        return 'All Hail King Steve'

@app.route("/delete/<name>")
def delete(name) :
	cur = mysql.connection.cursor()
	cur.execute('''DELETE from tasks WHERE taskName LIKE '%s' ''' % (name))
	cur.execute('commit;')
	return 'RIP STEVE'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')

@app.route('/lmao')
def root():
    return app.send_static_file('index.html')
