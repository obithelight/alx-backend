#!/usr/bin/env python3
''' This parametrizes the module templates '''

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    ''' The config class defined in 1-app.py '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    ''' renders the index page '''
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    ''' determines best match from supported languages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
