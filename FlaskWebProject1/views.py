"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
    )

@app.route('/activity')
def contact():
    """Renders the contact page."""
    return render_template(
        'activity.html',
        title='Activity',
        year=datetime.now().year,
        message='Games and Gamble.'
    )

@app.route('/leaderboard')
def about():
    """Renders the about page."""
    return render_template(
        'leaderboard.html',
        title='Leaderboard',
        year=datetime.now().year,
        message='Who is the man?'
    )

