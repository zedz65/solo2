from application import app
from flask import request, Response
# response is important to get a response
#normally import render template etc but not needed here as we dont use html
import random
import math
from random import randint

#specify 2 numbers and it picks a random int between the 2
@app.route('/generator/numbers', methods = ['GET'])
def sixdig():
    sixnum =  random.randint(100000,999999)
    return str(sixnum)
@app.route('/generator/8numbers', methods = ['GET'])
def eightdig():
    eightnum = random.randint(10000000,99999999)
    return str(eightnum)


print(sixdig())
print(eightdig())

