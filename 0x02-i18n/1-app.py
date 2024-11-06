#!/usr/bin/env python3
''' This module defines a basic babel setup'''

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    ''' This class sets babel's default locale and timezone '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    ''' This functin renders the index page '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
