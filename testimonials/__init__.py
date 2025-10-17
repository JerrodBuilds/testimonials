from flask import Flask #Brings the Flask class from the flask module allowing us to use it in our code

app = Flask(__name__) #Creates a new flask object and assigns it to a variable called app

import testimonials.routes