from flask import Blueprint

auth = Blueprint('auth', __name__)

#thats the way of declaring links on the site
@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>sign-up</p>"