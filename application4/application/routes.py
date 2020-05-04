from application import app
from flask import request, Response
# response is important to get a response
#normally import render template etc but not needed here as we dont use html
from random import randint
#specify 2 numbers and it picks a random int between the 2
@app.route('/prizeshort', methods = ['POST'])
def prizeshort():
    prizeusername = request.data.decode("utf-8")
    if prizeusername[0] == 'a':
        prize = "Congratulations! You won £100,000,000!"
    elif prizeusername[0] == 'b':
        prize = "Congratulations! You won £100,000,000!"
    elif prizeusername[0] == 'c':
        prize = "Congratulations! You won £100,000,000!"
    elif prizeusername[0] == 'd':
        prize = "Congratulations! You won £100,000,000!"
    elif prizeusername[0] == 'e':
        prize = "Congratulations! You won £100,000,000!"
    elif prizeusername[0] == 'f':
        prize = "Congratulations! You won £100,000,000!"
    else:
        prize = "Sorry, you didnt win anything this time."
    return Response(prize, mimetype= 'text/plain')

@app.route('/prizelong', methods = ['POST'])
def prizelong():
    prizeusername = request.data.decode("utf-8")
    if prizeusername[3] == '1':
        prize = "Congratulations, you won a £10 gift card!"
    elif prizeusername[3] == '2':
        prize = "Congratulations, you won a £10 gift card!"
    elif prizeusername[3] == '3':
        prize = "Congratulations, you won a £10 gift card!"
    elif prizeusername[3] == '4':
        prize = "Congratulations, you won a £10 gift card!"
    elif prizeusername[3] == '5':
        prize = "Congratulations, you won a £10 gift card!"
    elif prizeusername[3] == '6':
        prize = "Congratulations, you won a £10 gift card!"
    else:
        prize = "Try again next time"
    return Response(prize, mimetype= 'text/plain')
