##### Basic with end point
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def hello():
	name ="Harsh Mangal"
	return render_template("index.html" ,name1=name)
@app.route("/harsh")
def harsh():
	return render_template("harsh.html")
app.run(debug=True)