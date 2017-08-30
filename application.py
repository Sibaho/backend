from flask import Blueprint

application = Blueprint('application', __name__)

@application.route('/index')
@application.route('/')
def index():
    return 'Under Constructions!!!'

@application.route('/about')
def about():
    return 'About'