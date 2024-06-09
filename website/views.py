#in this file we wanna put everything that is realted to navigation of the site
from flask import Blueprint
#first variable defines name of the blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
# this function will run whenever user goes to /
    return "<h1>test</h1>"