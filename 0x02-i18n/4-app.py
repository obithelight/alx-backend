#!/usr/bin/env python3
''' forces and passes the locale=fr parameter to app URLs '''

from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    ''' configures the app '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    ''' renders the index page '''
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    ''' determine the best match with supported languages '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
