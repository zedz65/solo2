from application import app
from flask import request, Response
# response is important to get a response
#normally import render template etc but not needed here as we dont use html
import random
import math
from random import randint

#specify 2 numbers and it picks a random int between the 2
@app.route('/generator/numbers', methods = ['GET'])
def service3():
    numbergen =  random.randint(100,999)
    return str(numbergen)

print(str(service3()))

