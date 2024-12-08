from flask import Blueprint, render_template

bp_front = Blueprint('front_bp', __name__)

@bp_front.route('/')
def index():
    return render_template('home.html')


@bp_front.route('/up')
def up():
    return render_template('up.html')
