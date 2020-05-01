from application import app
from flask import request, Response
# response is important to get a response
#normally import render template etc but not needed here as we dont use html
from random import randint
#specify 2 numbers and it picks a random int between the 2
@app.route('/prizeshort', methods = ['POST'])
def prizeshort():
    if prizeusername[0] == 'a':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[0] == 'b':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[0] == 'c':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[0] == 'd':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[0] == 'e':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[0] == 'f':
        prize = "YOU ARE A WINNER!"
    else:
        prize = "Try again next time"
    return Response(prize, mimetype= 'text/plain')

@app.route('/prizelong', methods = ['POST'])
def prizelong():
    if prizeusername[3] == '1':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[3] == '2':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[3] == '3':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[3] == '4':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[3] == '5':
        prize = "YOU ARE A WINNER!"
    elif prizeusername[3] == '6':
        prize = "YOU ARE A WINNER!"
    else:
        prize = "Try again next time"
    return Response(prize, mimetype= 'text/plain')
