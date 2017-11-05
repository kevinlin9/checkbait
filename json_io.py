import sys

from flask import Flask, render_template, request, redirect, Response
import requests
from key import key

app = Flask(__name__)

comments_url = "https://www.googleapis.com/youtube/v3/commentThreads"

@app.route('/', methods = ['GET'])
def output():
	return render_template("index.html")

@app.route('/sendRequest/<string:query>')
def comments(query):
	#search_payload = {"key":key, "query": query}
	

if __name__ == '__main__':
	app.run()
