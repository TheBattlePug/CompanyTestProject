from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://mongo:27017")

@app.route("/")
def default():
	return render_template("page1.html")

@app.route("/page_1")
def page1():
	return render_template('page1.html')

@app.route("/page_2")
def page2():
	return render_template('page2.html')

@app.route("/page_3")
def page3():
	return render_template('page3.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=4000, debug=True)
