from flask import Flask,render_template
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "users_db"

mysql = MySQL(app)


@app.route('/', methods=['GET','POST'])

def index():

	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		age = request.form['age']
		location = request.form['location']

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO user (name,email,age,location) VALUES (%s,%s,%s,%s)",(username,email,age,location))

		mysql.connection.commit()
		cur.close()
		return "success"



	return render_template('index.html')


@app.route('/user')
def user():
	cur = mysql.connection.cursor()

	user = cur.execute("SELECT * FROM `user` ORDER BY `name` ASC")

	if user > 0:
		userDetails = cur.fetchall()

		return render_template('user.html', userDetails = userDetails)



if __name__ == "__main__":
	app.run(debug=True)
	