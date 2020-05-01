from application import app
from flask import request, Response
# response is important to get a response
#normally import render template etc but not needed here as we dont use html
from random import randint
#specify 2 numbers and it picks a random int between the 2

@app.route('/prize', methods = ['POST'])
def prizegen1():
    if accountnumber[0] == 'a':
        prize = "YOU ARE A WINNER!"    
    elif accountnumber[0] == 'b':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[0] == 'c':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[0] == 'd':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[0] == 'e':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[0] == 'f':
        prize = "YOU ARE A WINNER!"
    else:
        prize = "Try again next time"
    return Response(noise, mimetype= 'text/plain')

def prizegen2():
    if accountnumber[3] == '1':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[3] == '2':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[3] == '3':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[3] == '4':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[3] == '5':
        prize = "YOU ARE A WINNER!"
    elif accountnumber[3] == '6':
        prize = "YOU ARE A WINNER!"
    else:
        prize = "Try again next time"
    return Response(noise, mimetype= 'text/plain')
