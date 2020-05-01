from application import app
from flask import render_template, request, Response
import requests


@app.route('/', methods=['GET'])   
def home():

    three_lower = requests.get('http://application2:5001/generator/three_lower')	 
    get_sixdig = requests.get('http://application3:5002/generator/sixdig')
 
    return render_template('home.html', title='home', three_lower=three_lower.text, get_sixdig=get_sixdig.text) 


@app.route('/prize', methods=['GET'])
def prize():
    three_lower = requests.get('http://application2:5001/generator/three_lower')
    get_sixdig = requests.get('http://application3:5002/generator/sixdig')
    return render_template('prize.html', title='prize', three_lower=three_lower.text, get_sixdig=get_sixdig.text)

