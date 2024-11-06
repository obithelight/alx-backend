#!/usr/bin/env python3
''' This module defines a basic flask setup '''

from flask import Flask, render_template, request
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
    ''' This function renders the index page '''
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    '''
        Gets the locale from request and determines
        the best match with our supported languages
    '''
    return request.accept_languages.best_match(app.Config('LANGUAGES'))


if __name__ == '__main__':
    app.run(debug=True)
