from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route("/")
def gateway():
	ip = request.remote_addr
	return render_template("gateway.html")

@app.route("/index")
def index():
	ip = request.remote_addr

	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
