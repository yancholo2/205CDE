import pymysql
from flask import Flask,flash, render_template, request, redirect
from werkzeug import generate_password_hash, check_password_hash
from flask_table import Table, Col, LinkCol

app = Flask(__name__)
app.secret_key = "secret key"


db = pymysql.connect("localhost", "root", "9989", "example")

class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))

@app.route('/new_user')
def add_user_view():
	return render_template('add.html')
		
@app.route('/add', methods=['POST'])
def add_user():
	try:		
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _hashed_password,)
			db = mysql.connect()
			cursor = db.cursor()
			cursor.execute(sql, data)
			db.commit()
			flash('User added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		db.close()
		
@app.route('/')
def users():
	try:
		db = mysql.connect()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		db.close()

@app.route('/edit/<int:id>')
def edit_view(id):
	try:
		db = mysql.connect()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		db.close()

@app.route('/update', methods=['POST'])
def update_user():
	try:		
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		_id = request.form['id']
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (_name, _email, _hashed_password, _id,)
			db = mysql.connect()
			cursor = db.cursor()
			cursor.execute(sql, data)
			db.commit()
			flash('User updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		db.close()
		
@app.route('/delete/<int:id>')
def delete_user(id):
	try:
		db = mysql.connect()
		cursor = db.cursor()
		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
		db.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		db.close()
		
if __name__ == "__main__":
    app.run()