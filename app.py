import requests
from flask import Flask, request, render_template

'''Instantiation section'''
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

