from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Logger(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ip_address = db.Column(db.String(400))
	timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

	def __init__(self,ip_address):
		self.ip_address = ip_address

	def __repr__(self):
		return '<ip_addr %r>' % self.ip_address

@app.route("/")
def gateway():
	ip = request.remote_addr
	log = Logger(ip)
	db.session.add(log)
	db.session.commit()
	return render_template("gateway.html")

@app.route("/index")
def index():
	ip = request.remote_addr
	log = Logger(ip)
	db.session.add(log)
	db.session.commit()
	return render_template("index.html")

@app.route("/view_logs/<password>")
def view_logs(password):
	if password == "temporary_password":
		return render_template("viewer.html",results=Logger.query.all())
	else:
		return "Oh hi there"


if __name__ == '__main__':
	app.run(debug=True)
