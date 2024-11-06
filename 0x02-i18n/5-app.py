#!/usr/bin/env python3
''' forces and passes the locale=fr parameter to app URLs '''

from flask import Flask, request, render_template, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    ''' determine the best match with supported languages '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    ''' returns a user dictionary or None if ID not found '''
    user_id = request.args.get('login_as')

    if user_id:
        try:
            user_id = int(user_id)
            if user_id in users:
                return users[user_id]
            return None
        except Exception:
            return None


@app.before_request
def before_request():
    ''' finds and sets a user (if any) as global '''
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)
