from flask import Flask

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
        return 'Hello Admin'

@app.route("/user/<name>")

def hello_name():
        if name == 'admin':
        	return redirect(url_for('hello_admin'))
        else:
        	return redirect(url_for('hello_guest', guest = name))



if __name__ == '__main__':
        app.debug = True
        app.run(host="0.0.0.0", port=8000)
