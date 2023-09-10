from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route("/")
def home():
	return "This is a Home page"

@app.route("/senso")
def home2():
	return "This is a senso page"


@app.route("/page1")
def Page2():
	message="Page 1"
	return render_template("index.html",message=message)
	
if __name__=="__main__":
	app.run(debug=True, port=5000)
