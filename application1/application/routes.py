from application import app
from flask import render_template, request, Response
import requests


@app.route('/', methods=['GET'])   
def home():

    three_lower = requests.get('http://application2:5001/generator/three_lower')	 
    get_sixdig = requests.get('http://application3:5002/generator/sixdig')
    username = three_lower.text+str(get_sixdig.text)
    return render_template('home.html', title='home', username=username) 


@app.route('/prize/<prizeusername>', methods=['GET', 'POST'])
def prize(prizeusername):
    prize = requests.post('http://application4:5003/prizeshort/<prizeusername>', data=username)
    return render_template('prize.html', title='prize', prizeusername=username.text, prize=prize.text)

