from flask import Flask, render_template , request, url_for ,redirect , session
import pymysql
from flask import flash


app = Flask(__name__)
app.secret_key = 'Any string'

db = pymysql.connect("localhost", "root", "9989", "Store")

@app.route('/')



@app.route("/signup", methods = ['POST', 'GET'])
def signup():
	error = None
	if request.method == 'POST':
		usrname = request.form["username"]
		pwd =  request.form["password"]

		#prepare a cursor object using cursor() method
		cursor = db.cursor()
		
		cursor.execute("""INSERT INTO user (username, password) VALUES (%s, %s)""", (usrname, pwd))

		db.commit()
	return render_template("signup.html",test="success",error = error)

	db.close()
@app.route("/login", methods = ['POST', 'GET'])
def guest_login():
	error = None

	if request.method == 'POST':
		usrname = request.form["username"]
		pwd = request.form["password"]
		custName=[]
		custPassword=[]
		#
		cursor = db.cursor()

		#
		#
		sql = ("SELECT username, password FROM user WHERE username = '"+usrname+"'")
		cursor.execute(sql)
		#
		db.commit()
		results = cursor.fetchall()

		for row in results:
			custName.append(row[0])
			custPassword.append(row[1])
			#
		if custName ==[]:
			return render_template("login.html",test="Username Incorrect")
		if ('admin' == custName[0]) and ('admin' == custPassword[0]):
			session['logged_in'] = True
			return redirect(url_for('admin'))
		if (usrname == custName[0]) and (pwd == custPassword[0]):
			session['logged_in'] = True
			return redirect(url_for('store',guest = custName))
		elif usrname == custName[0] and pwd != custPassword[0]:
			return render_template("login.html",test="Password is incorrect. Please check the password!")

#		elif usrname != row[0]:return "<script>window.alert('Username does not sign up.')</script><a href= '/signup'>Click here to signup</a>"elif pwd != row[1]:return "<script>window.alert('Password is incorrect. Please check the password!.')</script><a href= '/login'>Click here to try again</a>"
	return render_template("login.html", error = error)

	db.close()

		#session["username"] = custNamereturn redirect(url_for('store', guest = custName))


#if usrname == "admin" and pwd == "admin":session["username"] = custNamereturn 

@app.route("/leave_question", methods = ['POST', 'GET'])
def leave_question():
	error = None
	if request.method == 'POST':
		emaildb = request.form["email"]
		questiondb =  request.form["question"]

		#prepare a cursor object using cursor() method
		cursor = db.cursor()
		
		cursor.execute("""INSERT INTO qa (email, question) VALUES (%s, %s)""", (emaildb, questiondb))

		db.commit()
		
	return render_template("contactus.html",error = error)

	db.close()

@app.route("/leave_request", methods = ['POST', 'GET'])
def leave_request():
	error = None
	if request.method == 'POST':
		un = request.form["username"]
		rt =  request.form["req"]

		#prepare a cursor object using cursor() method
		cursor = db.cursor()
		
		cursor.execute("""INSERT INTO requ (username, requests) VALUES (%s, %s)""", (un, rt))

		db.commit()
		
	return render_template("rrr.html",error = error)

	db.close()

@app.route("/payment", methods = ['POST', 'GET'])
def payment():
	error = None
	if request.method == 'POST':
		CN = request.form["cardnumber"]
		MM = request.form["mm"]
		YY = request.form["yy"]
		CV = request.form["cv"]
		NE = request.form["name"]
		AS = request.form["address"]



		#prepare a cursor object using cursor() method
		cursor = db.cursor()
		
		cursor.execute("""INSERT INTO pay (card, month, year, code, name, address) VALUES (%s, %s, %s, %s, %s, %s)""", (CN, MM, YY, CV, NE, AS))

		db.commit()
		
	return render_template("store.html",test="$128 Payed Thank You!")
	db.close()
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
	#
@app.route("/sign")
def sign():
	return render_template("signup.html")

@app.route("/admin")
def admin():
	return render_template("admin.html")

@app.route("/guest/<guest>")
def customer(guest):
	return 'Hello %s! ' % guest

@app.route("/about")
def about():
	return render_template("about us.html")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/contact")
def contact():
	return render_template("contactus.html")

@app.route("/store")
def store():
	return render_template("store.html")
def check():
	if not session.get('logged_in'):
		return render_template('login.html')

@app.route("/prepay")
def prepay():
	return render_template("prepay.html")
@app.route("/1st")
def first():
	return render_template("1stalbum.html")
@app.route("/2nd")
def second():
	return render_template("2ndalbum.html")
@app.route("/3rd")
def third():
	return render_template("3rdalbum.html")
@app.route("/4th")
def four():
	return render_template("4thalbum.html")
@app.route("/5th")
def five():
	return render_template("5thalbum.html")
@app.route("/6th")
def six():
	return render_template("6thalbum.html")

@app.route("/karaoke")
def karaoke():
	return render_template("karaoke.html")
@app.route("/rrr")
def rrr():
	return render_template("rrr.html")


if __name__ == '__main__':
        app.debug = True
        app.run(host="0.0.0.0", port=8000)

