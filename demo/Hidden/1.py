from flask import Flask, render_template
import pymysql
app = Flask(__name__)

db = pymysql.connect("localhost", "root", "9989", "Store")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS STUDENT1") 
sql= """CREATE TABLE STUDENT1 (FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, GENDER CHAR(1))"""
cursor.execute(sql)
db.close()