#in this file we wanna put everything that is realted to navigation of the site
from flask import Blueprint, render_template
#first variable defines name of the blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
# this function will run whenever user goes to /
    return render_template("home.html")