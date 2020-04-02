from flask import Blueprint, render_template

hello_page = Blueprint('hello_page', __name__)

@hello_page.route('/web/')
def hello():
    return render_template('hello.html')